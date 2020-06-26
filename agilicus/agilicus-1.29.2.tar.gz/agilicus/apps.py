import json
import urllib.parse
import agilicus
import requests

from . import context, response
from .input_helpers import build_updated_model
from .input_helpers import get_org_from_input_or_ctx


def _prepare_for_put(application):
    application.pop("id", None)
    application.pop("created", None)
    application.pop("updated", None)
    if "environments" in application:
        for env in application["environments"]:
            env.pop("application_services", None)


def query(ctx, org_id=None, maintained=None, **kwargs):
    token = context.get_token(ctx)

    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    params = {}

    if org_id:
        params["org_id"] = org_id
    else:
        org_id = context.get_org_id(ctx, token)
        if org_id:
            params["org_id"] = org_id
    if maintained:
        params["maintained"] = maintained

    query = urllib.parse.urlencode(params)
    uri = "/v2/applications?{}".format(query)
    resp = requests.get(
        context.get_api(ctx) + uri, headers=headers, verify=context.get_cacert(ctx),
    )
    response.validate(resp)
    return json.loads(resp.text)["applications"]


def get_app(ctx, org_id, application, **kwargs):
    for app in query(ctx, org_id, **kwargs):
        if app["name"] == application:
            return app


def _get_env_from_list(environments, name):
    for env in environments:
        if env["name"] == name:
            return env


def env_query(ctx, org_id, application, **kwargs):
    token = context.get_token(ctx)

    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    params = {}

    if org_id:
        params["org_id"] = org_id
    else:
        org_id = context.get_org_id(ctx, token)
        if org_id:
            params["org_id"] = org_id
    envs = []
    app = get_app(ctx, org_id, application)
    if not app:
        return envs
    environments = app.get("environments", envs)
    assignments = app.get("assignments", [])
    for assignment in assignments:
        _env = _get_env_from_list(environments, assignment["environment_name"])
        #  org = orgs.get(ctx, assignment['org_id'])
        _assignments = _env.get("assignments", [])
        _assignments.append(assignment["org_id"])
        # _assignments.append(org['organisation'])
        _env["assignments"] = _assignments
    return environments


def delete(ctx, id, org_id=None, **kwargs):
    token = context.get_token(ctx)

    params = {}
    if org_id:
        params["org_id"] = org_id
    else:
        org_id = context.get_org_id(ctx, token)
        if org_id:
            params["org_id"] = org_id
    query = urllib.parse.urlencode(params)

    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    uri = "/v2/applications/{}?{}".format(id, query)
    response = requests.delete(
        context.get_api(ctx) + uri, headers=headers, verify=context.get_cacert(ctx),
    )
    return response.text


def add(ctx, name, org_id, category):
    token = context.get_token(ctx)

    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    application = {}
    application["name"] = name
    application["org_id"] = org_id
    application["category"] = category

    uri = "/v2/applications"
    response = requests.post(
        context.get_api(ctx) + uri,
        headers=headers,
        json=application,
        verify=context.get_cacert(ctx),
    )
    return response.text


def _find_item(items, key, keyval):
    for item in items:
        if item[key] == keyval:
            return item
    return None


def add_role(ctx, id, role_name):
    token = context.get_token(ctx)

    application = json.loads(get(ctx, id))
    # We can't put the id
    del application["id"]
    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    roles = application.get("roles")
    _prepare_for_put(application)

    if not _find_item(roles, "name", role_name):
        roles.append({"name": role_name, "rules": []})

    uri = "/v2/applications/{}".format(id)
    resp = requests.put(
        context.get_api(ctx) + uri,
        headers=headers,
        json=application,
        verify=context.get_cacert(ctx),
    )
    response.validate(resp)
    return resp.text


def add_definition(ctx, id, key, path):
    token = context.get_token(ctx)

    application = json.loads(get(ctx, id))
    # We can't put the id
    del application["id"]
    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    definitions = application.get("definitions")
    definition = _find_item(definitions, "key", key)
    if not definition:
        definition = {"key": key}
        definitions.append(definition)

    definition["value"] = path

    uri = "/v2/applications/{}".format(id)
    resp = requests.put(
        context.get_api(ctx) + uri,
        headers=headers,
        json=application,
        verify=context.get_cacert(ctx),
    )
    response.validate(resp)
    return resp.text


def _build_rule(
    rules,
    name,
    method,
    path,
    query_parameters: list,
    json_pointers: list,
    host=None,
    rule_name=None,
):
    rule = {}
    rule["name"] = name
    if host:
        rule["host"] = host
    rule["method"] = method
    rule["path"] = path
    rendered_params = []
    if query_parameters:
        for name, exact_match in query_parameters:
            rendered_params.append({"name": name, "exact_match": exact_match})
        rule["query_parameters"] = rendered_params

    if json_pointers:
        body = rule.setdefault("body", {})
        json_pointer = body.setdefault("json", [])
        for pointer in json_pointers:
            json_pointer.append(
                {
                    "pointer": pointer[0],
                    "exact_match": pointer[1],
                    "name": str(len(json_pointer) + 1),
                    "match_type": "string",
                }
            )
        rule["body"] = body

    for existing_rule in rules:
        if existing_rule["name"] == name:
            rules.remove(existing_rule)

    return rule


def add_rule(
    ctx,
    app_name,
    role_name,
    method,
    path,
    query_parameters: list,
    json_pointers: list,
    rule_name=None,
    host=None,
    org_id=None,
):
    token = context.get_token(ctx)

    if not org_id:
        org_id = context.get_org_id(ctx, token)

    application = get_app(ctx, org_id, app_name)
    if not application:
        raise Exception(f"Application {app_name} not found")

    id = application["id"]
    # We can't put the id
    del application["id"]
    del application["created"]
    if "updated" in application:
        del application["updated"]
    # This is rather gross. We can't put the application_services
    # into the put request since it is read-only
    if "environments" in application:
        for env in application["environments"]:
            if "application_services" in env:
                del env["application_services"]

    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    roles = application.get("roles")
    role = _find_item(roles, "name", role_name)
    if not role:
        # Maybe we should not handle this case...
        role = {"name": role_name, "rules": []}
        roles.append(role)

    rules = role["rules"]
    if not rule_name:
        rule_name = str(len(rules) + 1)

    new_rule = _build_rule(
        rules, rule_name, method, path, query_parameters, json_pointers, host, rule_name,
    )
    rules.append(new_rule)

    uri = "/v2/applications/{}".format(id)
    resp = requests.put(
        context.get_api(ctx) + uri,
        headers=headers,
        json=application,
        verify=context.get_cacert(ctx),
    )
    response.validate(resp)
    return resp.text


def delete_rule(ctx, app_name, role_name, rule_name, org_id=None):
    token = context.get_token(ctx)

    if not org_id:
        org_id = context.get_org_id(ctx, token)

    application = get_app(ctx, org_id, app_name)
    if not application:
        raise Exception(f"Application {app_name} not found")

    _roles = []
    for role in application.get("roles", []):
        _rules = role.get("rules", [])
        if role["name"] == role_name:
            _update_rules = []
            for rule in _rules:
                if rule["name"] == rule_name:
                    continue
                _update_rules.append(rule)
            _rules = _update_rules
        role["rules"] = _rules
        _roles.append(role)
    application["roles"] = _roles

    id = application["id"]
    # We can't put the id
    del application["id"]
    del application["created"]
    if "updated" in application:
        del application["updated"]
    # This is rather gross. We can't put the application_services
    # into the put request since it is read-only
    if "environments" in application:
        for env in application["environments"]:
            if "application_services" in env:
                del env["application_services"]

    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)
    uri = "/v2/applications/{}".format(id)
    resp = requests.put(
        context.get_api(ctx) + uri,
        headers=headers,
        json=application,
        verify=context.get_cacert(ctx),
    )
    response.validate(resp)
    return resp.text


def get_roles(ctx, app_name, org_id=None):
    token = context.get_token(ctx)

    if not org_id:
        org_id = context.get_org_id(ctx, token)

    _app = get_app(ctx, org_id, app_name)
    if not _app:
        raise Exception(f"Application {app_name} not found")

    _roles = _app.get("roles", [])
    for _role in _roles:
        _role["rules"] = sorted(_role["rules"], key=lambda k: k["name"])
    return _roles


def _get(ctx, id, org_id=None):
    token = context.get_token(ctx)

    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    uri = "/v2/applications/{}".format(id)
    if org_id:
        uri = f"{uri}?org_id={org_id}"
    else:
        org_id = context.get_org_id(ctx, token)
        if org_id:
            uri = f"{uri}?org_id={org_id}"

    resp = requests.get(
        context.get_api(ctx) + uri, headers=headers, verify=context.get_cacert(ctx),
    )
    response.validate(resp)
    return resp.json()


def get(ctx, id, **kwargs):
    return json.dumps(_get(ctx, id))


def get_env(ctx, application, env_name, org_id=None, **kwargs):
    token = context.get_token(ctx)
    if not org_id:
        org_id = context.get_org_id(ctx, token)

    app = get_app(ctx, org_id, application)

    apiclient = context.get_apiclient(ctx, token)
    return apiclient.application_api.get_environment(
        app["id"], env_name, org_id
    ).to_dict()


def update_env(
    ctx,
    id,
    env_name,
    org_id=None,
    version_tag=None,
    config_mount_path=None,
    config_as_mount=None,
    config_as_env=None,
    secrets_mount_path=None,
    secrets_as_mount=None,
    secrets_as_env=None,
    serverless_image=None,
    **kwargs,
):
    token = context.get_token(ctx)
    if not org_id:
        org_id = context.get_org_id(ctx, token)
    apiclient = context.get_apiclient(ctx, token)
    app_env = apiclient.application_api.get_environment(id, env_name, org_id)

    if version_tag:
        app_env.version_tag = version_tag

    if config_mount_path is not None:
        app_env.config_mount_path = config_mount_path

    if config_as_mount is not None:
        app_env.config_as_mount = config_as_mount

    if config_as_env is not None:
        app_env.config_as_env = config_as_env

    if secrets_mount_path is not None:
        app_env.secrets_mount_path = secrets_mount_path

    if secrets_as_mount is not None:
        app_env.secrets_as_mount = secrets_as_mount

    if secrets_as_env is not None:
        app_env.secrets_as_env = secrets_as_env

    if serverless_image is not None:
        app_env.serverless_image = serverless_image

    app_env.application_services = None

    apiclient.application_api.replace_environment(id, env_name, environment=app_env)


def add_basic_environment(app_object, env_name, admin_org_id=None):
    environs = app_object.setdefault("environments", [])
    for environ in environs:
        if environ["name"] == env_name:
            return

    environ = {}
    environ["name"] = env_name
    environ["version_tag"] = "latest"
    if admin_org_id:
        environ["maintenance_org_id"] = admin_org_id
    environs.append(environ)


def _remove_env(app_object, env_name):
    environs = app_object.setdefault("environments", [])
    new_environs = []
    for environ in environs:
        if environ["name"] == env_name:
            continue
        else:
            new_environs.append(environ)
    app_object["environments"] = new_environs


def _update_env_assignment(app_object, env_name, org_id, unassign=False):
    assignments = app_object.setdefault("assignments", [])
    update_assignments = []
    for assignment in assignments:
        name = assignment["environment_name"]
        id = assignment["org_id"]
        if name == env_name and id == org_id:
            if unassign:
                continue
            else:
                return
        else:
            update_assignments.append(assignment)

    if not unassign:
        assignment = {}
        assignment["environment_name"] = env_name
        assignment["org_id"] = org_id
        update_assignments.append(assignment)
    app_object["assignments"] = update_assignments


def update_assignment(
    ctx, env_name, app_id, org_id, sub_org_id, unassign=False, admin_org_id=None,
):
    token = context.get_token(ctx)

    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    application = _get(ctx, app_id, org_id=org_id)
    add_basic_environment(application, env_name, admin_org_id)
    _update_env_assignment(application, env_name, sub_org_id, unassign)
    _prepare_for_put(application)

    uri = f"/v2/applications/{app_id}"
    response = requests.put(
        context.get_api(ctx) + uri,
        headers=headers,
        json=application,
        verify=context.get_cacert(ctx),
    )
    return response.text


def delete_environment(ctx, env_name, app_id, org_id):
    token = context.get_token(ctx)

    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    application = _get(ctx, app_id, org_id=org_id)
    _remove_env(application, env_name)
    _prepare_for_put(application)

    uri = f"/v2/applications/{app_id}"
    response = requests.put(
        context.get_api(ctx) + uri,
        headers=headers,
        json=application,
        verify=context.get_cacert(ctx),
    )
    return response.text


def update_application(ctx, app_id, org_id, image=None, port=None):
    token = context.get_token(ctx)

    if not org_id:
        org_id = context.get_org_id(ctx, token)

    headers = {}
    headers["Authorization"] = "Bearer {}".format(token)

    application = _get(ctx, app_id, org_id=org_id)

    if image:
        application["image"] = image
    if port:
        application["port"] = port

    _prepare_for_put(application)

    uri = f"/v2/applications/{app_id}"
    resp = requests.put(
        context.get_api(ctx) + uri,
        headers=headers,
        json=application,
        verify=context.get_cacert(ctx),
    )
    response.validate(resp)
    return resp.text


def get_application_services(ctx, org_id=None, **kwargs):
    token = context.get_token(ctx)
    if not org_id:
        org_id = context.get_org_id(ctx, token)
    apiclient = context.get_apiclient(ctx, token)
    return apiclient.app_services_api.list_application_services(
        org_id
    ).application_services


def get_application_service(ctx, id, org_id=None, **kwargs):
    token = context.get_token(ctx)
    if not org_id:
        org_id = context.get_org_id(ctx, token)
    apiclient = context.get_apiclient(ctx, token)
    return apiclient.app_services_api.get_application_service(id, org_id)


def add_application_service(
    ctx,
    name,
    hostname,
    port,
    org_id=None,
    ipv4_addresses=None,
    name_resolution=None,
    protocol=None,
):
    token = context.get_token(ctx)
    if not org_id:
        org_id = context.get_org_id(ctx, token)
    apiclient = context.get_apiclient(ctx, token)
    if ipv4_addresses:
        ipv4_addresses = ipv4_addresses.split(",")

    service = agilicus.ApplicationService(
        name=name,
        org_id=org_id,
        hostname=hostname,
        port=port,
        ipv4_addresses=ipv4_addresses,
        name_resolution=name_resolution,
        protocol=protocol,
    )
    return apiclient.app_services_api.post_application_service(service)


def update_application_service(
    ctx,
    id,
    name=None,
    hostname=None,
    port=None,
    org_id=None,
    ipv4_addresses=None,
    name_resolution=None,
    protocol=None,
):

    token = context.get_token(ctx)
    if not org_id:
        org_id = context.get_org_id(ctx, token)
    apiclient = context.get_apiclient(ctx, token)

    service = apiclient.app_services_api.get_application_service(id, org_id)

    if name:
        service.name = name
    if hostname:
        service.hostname = hostname
    if port:
        service.port = port
    if ipv4_addresses:
        service.ipv4_addresses = ipv4_addresses.split(",")
    if name_resolution:
        service.name_resolution = name_resolution
    if protocol:
        service.protocol = protocol

    service.id = None

    return apiclient.app_services_api.replace_application_service(
        id, application_service=service
    )


def _get_app_service(ctx, org_id, name):
    for _service in get_application_services(ctx, org_id):
        if _service.name == name:
            return _service


def add_application_service_assignment(
    ctx, app_service_name, app_name, environment_name, org_id=None
):
    token = context.get_token(ctx)
    if not org_id:
        org_id = context.get_org_id(ctx, token)
    apiclient = context.get_apiclient(ctx, token)

    service = _get_app_service(ctx, org_id, app_service_name)
    if not service:
        raise Exception(f"Application service {app_service_name} not found")

    _app = get_app(ctx, org_id, app_name)
    if not _app:
        raise Exception(f"Application {app_name} not found")

    id = service.id
    service.id = None
    assignment = agilicus.ApplicationServiceAssignment(
        app_id=_app["id"], environment_name=environment_name, org_id=_app["org_id"],
    )

    service.assignments.append(assignment)
    return apiclient.app_services_api.replace_application_service(
        id, application_service=service
    )


def delete_application_service_assignment(
    ctx, app_service_name, app_name, environment_name, org_id=None
):
    token = context.get_token(ctx)
    if not org_id:
        org_id = context.get_org_id(ctx, token)
    apiclient = context.get_apiclient(ctx, token)

    service = _get_app_service(ctx, org_id, app_service_name)
    if not service:
        raise Exception(f"Application service {app_service_name} not found")

    _app = get_app(ctx, org_id, app_name)
    if not _app:
        raise Exception(f"Application {app_name} not found")

    id = service.id
    service.id = None
    new_list = []
    for assignment in service.assignments:
        if (
            assignment.app_id == _app["id"]
            and assignment.environment_name == environment_name
            and assignment.org_id == _app["org_id"]
        ):
            pass
        else:
            new_list.append(assignment)

    service.assignments = new_list
    return apiclient.app_services_api.replace_application_service(
        id, application_service=service
    )


def delete_application_service(ctx, name, org_id=None, **kwargs):
    token = context.get_token(ctx)
    if not org_id:
        org_id = context.get_org_id(ctx, token)
    apiclient = context.get_apiclient(ctx, token)
    return apiclient.app_services_api.delete_application_service(name, org_id)


def list_app_rules(ctx, app_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    query_results = apiclient.application_api.list_rules(app_id, **kwargs)
    if query_results:
        return query_results.rules
    return []


def construct_rule_model(app_id, **kwargs):
    condition = agilicus.HttpRule(
        rule_type=kwargs.get("rule_type", None),
        methods=kwargs.get("methods", None),
        path_regex=kwargs.get("path_regex", None),
    )
    spec = agilicus.RuleSpec(
        app_id=app_id,
        comments=kwargs.get("comments", None),
        condition=condition,
        org_id=kwargs.get("org_id", None),
        scope=kwargs.get("rule_scope", None),
    )
    model = agilicus.RuleV2(spec=spec)
    return model


def add_http_rule(ctx, app_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    model = construct_rule_model(app_id, **kwargs)
    return apiclient.application_api.add_rule(app_id, model).to_dict()


def _get_rule_v2(ctx, apiclient, app_id, rule_id, **kwargs):
    org_id = get_org_from_input_or_ctx(ctx, **kwargs)
    return apiclient.application_api.get_rule(app_id, rule_id, org_id=org_id)


def show_rule_v2(ctx, app_id, rule_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    return _get_rule_v2(ctx, apiclient, app_id, rule_id, **kwargs).to_dict()


def delete_rule_v2(ctx, app_id, rule_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    org_id = get_org_from_input_or_ctx(ctx, **kwargs)
    return apiclient.application_api.delete_rule(app_id, rule_id, org_id=org_id)


def update_conditions(rule, kwargs):
    updates_to_apply = {}
    updates_to_apply["path_regex"] = kwargs.pop("path_regex", None)
    updates_to_apply["rule_type"] = kwargs.pop("rule_type", None)
    return build_updated_model(agilicus.HttpRule, rule.spec.condition, updates_to_apply)


def update_http_rule(
    ctx, app_id, rule_id, query_params=None, body_params=None, methods=None, **kwargs
):
    apiclient = context.get_apiclient_from_ctx(ctx)
    rule = _get_rule_v2(ctx, apiclient, app_id, rule_id, **kwargs)
    rule.spec.condition = update_conditions(rule, kwargs)
    rule.spec = build_updated_model(agilicus.RuleSpec, rule.spec, kwargs)
    if query_params is not None:
        rule.spec.condition["query_parameters"] = [
            agilicus.RuleQueryParameter(*tup) for tup in query_params
        ]
    if body_params is not None:
        rule.spec.condition["body"]["json"] = [
            agilicus.RuleQueryBodyJSON(*tup) for tup in body_params
        ]
    if methods is not None:
        rule.spec.condition["methods"] = [method for method in methods]
    return apiclient.application_api.replace_rule(
        app_id, rule_id, rule_v2=rule
    ).to_dict()


def list_combined_rules(ctx, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    if "app_id" in kwargs and kwargs["app_id"] is None:
        kwargs.pop("app_id")
    query_results = apiclient.application_api.list_combined_rules(**kwargs)
    if query_results:
        return query_results.combined_rules
    return []


def list_roles(ctx, app_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    query_results = apiclient.application_api.list_roles(app_id, **kwargs)
    if query_results:
        return query_results.roles
    return []


def add_role_v2(ctx, app_id, name, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    included = kwargs.pop("included", None)
    if included:
        included_model = [agilicus.IncludedRole(role_id=id) for id in included]
    spec = agilicus.RoleSpec(app_id, name, included=included_model, **kwargs)
    model = agilicus.RoleV2(spec=spec)
    return apiclient.application_api.add_role(app_id, model).to_dict()


def _get_role_by_id(ctx, apiclient, app_id, role_id, **kwargs):
    kwargs["org_id"] = get_org_from_input_or_ctx(ctx, **kwargs)
    return apiclient.application_api.get_role(app_id, role_id, **kwargs)


def show_role_v2(ctx, app_id, role_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    return _get_role_by_id(ctx, apiclient, app_id, role_id, **kwargs).to_dict()


def delete_role_v2(ctx, app_id, role_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    kwargs["org_id"] = get_org_from_input_or_ctx(ctx, **kwargs)
    return apiclient.application_api.delete_role(app_id, role_id, **kwargs)


def update_role_v2(ctx, app_id, role_id, included=None, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    role = _get_role_by_id(ctx, apiclient, app_id, role_id)
    role.spec = build_updated_model(agilicus.RoleSpec, role.spec, kwargs)
    if included is not None:
        role.spec.included = [agilicus.IncludedRole(role_id=id) for id in included]
    return apiclient.application_api.replace_role(
        app_id, role_id, role_v2=role
    ).to_dict()


def list_roles_to_rules(ctx, app_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    query_results = apiclient.application_api.list_role_to_rule_entries(app_id, **kwargs)
    if query_results:
        return query_results.role_to_rule_entries
    return []


def add_role_to_rule(ctx, app_id, role_id, rule_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    spec = agilicus.RoleToRuleEntrySpec(
        app_id=app_id, role_id=role_id, rule_id=rule_id, **kwargs
    )
    model = agilicus.RoleToRuleEntry(spec=spec)
    return apiclient.application_api.add_role_to_rule_entry(app_id, model).to_dict()


def _get_role_to_rule(ctx, apiclient, app_id, role_to_rule_id, **kwargs):
    keyword_args = {}
    keyword_args["org_id"] = get_org_from_input_or_ctx(ctx, **kwargs)
    return apiclient.application_api.get_role_to_rule_entry(
        app_id, role_to_rule_id, **keyword_args
    )


def show_role_to_rule(ctx, app_id, role_to_rule_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    return _get_role_to_rule(ctx, apiclient, app_id, role_to_rule_id, **kwargs).to_dict()


def delete_role_to_rule(ctx, app_id, role_to_rule_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    kwargs["org_id"] = get_org_from_input_or_ctx(ctx, **kwargs)
    return apiclient.application_api.delete_role_to_rule_entry(
        app_id, role_to_rule_id, **kwargs
    )


def update_role_to_rule(ctx, app_id, role_to_rule_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    mapping = _get_role_to_rule(ctx, apiclient, app_id, role_to_rule_id, **kwargs)

    mapping.spec = build_updated_model(
        agilicus.RoleToRuleEntrySpec, mapping.spec, kwargs
    )
    return apiclient.application_api.replace_role_to_rule_entry(
        app_id, role_to_rule_id, role_to_rule_entry=mapping
    ).to_dict()
