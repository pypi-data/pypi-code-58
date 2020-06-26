from __future__ import absolute_import

import io
import os
import uuid

import nbformat
from dagster_graphql.implementation.context import DagsterGraphQLContext
from dagster_graphql.schema import create_schema
from dagster_graphql.version import __version__ as dagster_graphql_version
from flask import Flask, jsonify, redirect, request, send_file
from flask_cors import CORS
from flask_graphql import GraphQLView
from flask_sockets import Sockets
from graphql.execution.executors.gevent import GeventExecutor as Executor
from nbconvert import HTMLExporter

from dagster import __version__ as dagster_version
from dagster import check, seven
from dagster.cli.workspace import Workspace
from dagster.core.definitions.reconstructable import ReconstructableRepository
from dagster.core.execution.compute_logs import warn_if_compute_logs_disabled
from dagster.core.host_representation import (
    InProcessRepositoryLocation,
    PythonEnvRepositoryLocation,
)
from dagster.core.host_representation.handle import (
    InProcessRepositoryLocationHandle,
    PythonEnvRepositoryLocationHandle,
)
from dagster.core.instance import DagsterInstance
from dagster.core.storage.compute_log_manager import ComputeIOType

from .format_error import format_error_with_stack_trace
from .subscription_server import DagsterSubscriptionServer
from .templates.playground import TEMPLATE as PLAYGROUND_TEMPLATE
from .version import __version__

MISSING_SCHEDULER_WARNING = (
    'You have defined ScheduleDefinitions for this repository, but have '
    'not defined a scheduler on the instance'
)


class DagsterGraphQLView(GraphQLView):
    def __init__(self, context, **kwargs):
        super(DagsterGraphQLView, self).__init__(**kwargs)
        self.context = check.inst_param(context, 'context', DagsterGraphQLContext)

    def get_context(self):
        return self.context

    format_error = staticmethod(format_error_with_stack_trace)


def dagster_graphql_subscription_view(subscription_server, context):
    context = check.inst_param(context, 'context', DagsterGraphQLContext)

    def view(ws):
        subscription_server.handle(ws, request_context=context)
        return []

    return view


def info_view():
    return (
        jsonify(
            dagit_version=__version__,
            dagster_graphql_version=dagster_graphql_version,
            dagster_version=dagster_version,
        ),
        200,
    )


def index_view(_path):
    try:
        return send_file(os.path.join(os.path.dirname(__file__), './webapp/build/index.html'))
    except seven.FileNotFoundError:
        text = '''<p>Can't find webapp files. Probably webapp isn't built. If you are using
        dagit, then probably it's a corrupted installation or a bug. However, if you are
        developing dagit locally, your problem can be fixed as follows:</p>

<pre>cd ./python_modules/
make rebuild_dagit</pre>'''
        return text, 500


def notebook_view(request_args):
    check.dict_param(request_args, 'request_args')

    # This currently provides open access to your file system - the very least we can
    # do is limit it to notebook files until we create a more permanent solution.
    path = request_args['path']
    if not path.endswith('.ipynb'):
        return 'Invalid Path', 400

    with open(os.path.abspath(path)) as f:
        read_data = f.read()
        notebook = nbformat.reads(read_data, as_version=4)
        html_exporter = HTMLExporter()
        html_exporter.template_file = 'basic'
        (body, resources) = html_exporter.from_notebook_node(notebook)
        return '<style>' + resources['inlining']['css'][0] + '</style>' + body, 200


def download_view(context):
    context = check.inst_param(context, 'context', DagsterGraphQLContext)

    def view(run_id, step_key, file_type):
        run_id = str(uuid.UUID(run_id))  # raises if not valid run_id
        step_key = step_key.split('/')[-1]  # make sure we're not diving deep into
        out_name = '{}_{}.{}'.format(run_id, step_key, file_type)

        manager = context.instance.compute_log_manager
        try:
            io_type = ComputeIOType(file_type)
            result = manager.get_local_path(run_id, step_key, io_type)
            if not os.path.exists(result):
                result = io.BytesIO()
            timeout = None if manager.is_watch_completed(run_id, step_key) else 0
        except ValueError:
            result = io.BytesIO()
            timeout = 0

        if not result:
            result = io.BytesIO()

        return send_file(
            result, as_attachment=True, attachment_filename=out_name, cache_timeout=timeout
        )

    return view


def instantiate_app_with_views(context):
    app = Flask(
        'dagster-ui',
        static_url_path='',
        static_folder=os.path.join(os.path.dirname(__file__), './webapp/build'),
    )
    sockets = Sockets(app)
    app.app_protocol = lambda environ_path_info: 'graphql-ws'

    schema = create_schema()
    subscription_server = DagsterSubscriptionServer(schema=schema)

    app.add_url_rule(
        '/graphql',
        'graphql',
        DagsterGraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True,
            # XXX(freiksenet): Pass proper ws url
            graphiql_template=PLAYGROUND_TEMPLATE,
            executor=Executor(),
            context=context,
        ),
    )
    app.add_url_rule('/graphiql', 'graphiql', lambda: redirect('/graphql', 301))
    sockets.add_url_rule(
        '/graphql', 'graphql', dagster_graphql_subscription_view(subscription_server, context)
    )

    app.add_url_rule(
        # should match the `build_local_download_url`
        '/download/<string:run_id>/<string:step_key>/<string:file_type>',
        'download_view',
        download_view(context),
    )

    # these routes are specifically for the Dagit UI and are not part of the graphql
    # API that we want other people to consume, so they're separate for now.
    # Also grabbing the magic global request args dict so that notebook_view is testable
    app.add_url_rule('/dagit/notebook', 'notebook', lambda: notebook_view(request.args))

    app.add_url_rule('/dagit_info', 'sanity_view', info_view)
    app.register_error_handler(404, index_view)
    CORS(app)
    return app


def create_app_from_workspace(workspace, instance):
    check.inst_param(workspace, 'workspace', Workspace)
    check.inst_param(instance, 'instance', DagsterInstance)

    warn_if_compute_logs_disabled()

    print('Loading repository...')

    locations = []
    for repository_location_handle in workspace.repository_location_handles:
        if isinstance(repository_location_handle, InProcessRepositoryLocationHandle):
            # will need to change for multi repo
            check.invariant(len(repository_location_handle.repository_code_pointer_dict) == 1)
            pointer = next(iter(repository_location_handle.repository_code_pointer_dict.values()))
            recon_repo = ReconstructableRepository(pointer)
            locations.append(InProcessRepositoryLocation(recon_repo))
        elif isinstance(repository_location_handle, PythonEnvRepositoryLocationHandle):
            locations.append(PythonEnvRepositoryLocation(repository_location_handle))
        else:
            check.failed('{} unsupported'.format(repository_location_handle))

    context = DagsterGraphQLContext(instance=instance, locations=locations, version=__version__)

    return instantiate_app_with_views(context)
