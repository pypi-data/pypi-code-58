# -*- coding: utf-8 -*-
#
# Copyright 2018-2020- Swiss Data Science Center (SDSC)
# A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
# Eidgenössische Technische Hochschule Zürich (ETHZ).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""Show information about objects in current repository.

Siblings
~~~~~~~~

In situations when multiple outputs have been generated by a single
``renku run`` command, the siblings can be discovered by running
``renku show siblings PATH`` command.

Assume that the following graph represents relations in the repository.

.. code-block:: text

          D---E---G
         /     \
    A---B---C   F

Then the following outputs would be shown.

.. code-block:: console

   $ renku show siblings C
   C
   D
   $ renku show siblings G
   F
   G
   $ renku show siblings A
   A
   $ renku show siblings C G
   C
   D
   ---
   F
   G
   $ renku show siblings
   A
   ---
   B
   ---
   C
   D
   ---
   E
   ---
   F
   G

You can use the ``-f`` or ``--flat`` flag to output a flat list, as well as
the ``-v`` or ``--verbose`` flag to also output commit information.


Input and output files
~~~~~~~~~~~~~~~~~~~~~~

You can list input and output files generated in the repository by running
``renku show inputs`` and ``renku show outputs`` commands. Alternatively,
you can check if all paths specified as arguments are input or output files
respectively.

.. code-block:: console

   $ renku run wc < source.txt > result.wc
   $ renku show inputs
   source.txt
   $ renku show outputs
   result.wc
   $ renku show outputs source.txt
   $ echo $?  # last command finished with an error code
   1

"""

import click

from renku.core import errors
from renku.core.commands.client import pass_local_client
from renku.core.commands.graph import Graph
from renku.core.models.entities import Entity


@click.group()
def show():
    """Show information about objects in a current repository.

    NOTE: The command produces a machine-readable output.
    """
    pass


@show.command()
@click.option('--revision', default='HEAD')
@click.option('-f', '--flat', is_flag=True)
@click.option('-v', '--verbose', is_flag=True)
@click.argument(
    'paths', type=click.Path(exists=True, dir_okay=False), nargs=-1
)
@pass_local_client(requires_migration=True)
def siblings(client, revision, flat, verbose, paths):
    """Show siblings for given paths."""
    graph = Graph(client)
    nodes = graph.build(paths=paths, revision=revision)
    nodes = [n for n in nodes if not isinstance(n, Entity) or n.parent]

    sibling_sets = {frozenset([n]) for n in set(nodes)}
    for node in nodes:
        try:
            sibling_sets.add(frozenset(graph.siblings(node)))
        except (errors.InvalidOutputPath):
            # ignore nodes that aren't outputs if no path was supplied
            if paths:
                raise
            else:
                sibling_sets.discard({node})

    result_sets = []
    for candidate in sibling_sets:
        new_result = []

        for result in result_sets:
            if candidate & result:
                candidate |= result
            else:
                new_result.append(result)

        result_sets = new_result
        result_sets.append(candidate)

    result = [[sibling_name(graph, node, verbose) for node in r]
              for r in result_sets]

    if flat:
        click.echo('\n'.join({n for r in result for n in r}))
    else:
        click.echo('\n---\n'.join('\n'.join(r) for r in result))


@show.command()
@click.option('--revision', default='HEAD')
@click.argument(
    'paths',
    type=click.Path(exists=True, dir_okay=False),
    nargs=-1,
)
@pass_local_client(requires_migration=True)
@click.pass_context
def inputs(ctx, client, revision, paths):
    r"""Show inputs files in the repository.

    <PATHS>    Files to show. If no files are given all input files are shown.
    """
    from renku.core.models.provenance.activities import ProcessRun

    graph = Graph(client)
    paths = set(paths)
    nodes = graph.build(revision=revision)

    commits = {node.commit for node in nodes}
    candidates = {(node.commit, node.path)
                  for node in nodes if not paths or node.path in paths}

    input_paths = set()

    for commit in commits:
        activity = graph.activities[commit]

        if isinstance(activity, ProcessRun):
            for usage in activity.qualified_usage:
                for entity in usage.entity.entities:
                    path = str((usage.client.path / entity.path).relative_to(
                        client.path
                    ))
                    usage_key = (entity.commit, entity.path)

                    if path not in input_paths and usage_key in candidates:
                        input_paths.add(path)

    click.echo('\n'.join(graph._format_path(path) for path in input_paths))
    ctx.exit(0 if not paths or len(input_paths) == len(paths) else 1)


@show.command()
@click.option('--revision', default='HEAD')
@click.argument(
    'paths',
    type=click.Path(exists=True, dir_okay=True),
    nargs=-1,
)
@pass_local_client(requires_migration=True)
@click.pass_context
def outputs(ctx, client, revision, paths):
    r"""Show output files in the repository.

    <PATHS>    Files to show. If no files are given all output files are shown.
    """
    graph = Graph(client)
    filter = graph.build(paths=paths, revision=revision)
    output_paths = graph.output_paths

    click.echo('\n'.join(graph._format_path(path) for path in output_paths))

    if paths:
        if not output_paths:
            ctx.exit(1)

        from renku.core.models.datastructures import DirectoryTree
        tree = DirectoryTree.from_list(item.path for item in filter)

        for output in output_paths:
            if tree.get(output) is None:
                ctx.exit(1)
                return


def sibling_name(graph, node, verbose=False):
    """Return the display name of a sibling."""
    name = graph._format_path(node.path)

    if verbose:
        name = '{} @ {}'.format(name, node.commit)

    return name


def _context_names():
    """Return list of valid context names."""
    from renku.core.models.jsonld import JSONLDMixin

    # NOTE: You should only pass a list or tuple of choices. Other iterables
    # (like generators) may lead to surprising results.
    return [cls.__name__ for cls in JSONLDMixin.__type_registry__.values()]


def print_context_names(ctx, param, value):
    """Print all possible types."""
    if not value or ctx.resilient_parsing:
        return
    click.echo('\n'.join(_context_names()))
    ctx.exit()


def _context_json(name):
    """Return JSON-LD string for given context name."""
    from renku.core.models.jsonld import JSONLDMixin

    for cls in JSONLDMixin.__type_registry__.values():
        if cls.__name__ == name:
            return {
                '@context': cls._jsonld_context,
                '@type': cls._jsonld_type,
            }


@show.command()
@click.argument(
    'names',
    type=click.Choice(_context_names()),
    nargs=-1,
)
@click.option(
    '--list',
    is_flag=True,
    is_eager=True,
    expose_value=False,
    callback=print_context_names,
    help=print_context_names.__doc__,
)
def context(names):
    """Show JSON-LD context for repository objects."""
    import json

    contexts = [_context_json(name) for name in set(names)]
    if contexts:
        click.echo(
            json.dumps(
                contexts[0] if len(contexts) == 1 else contexts,
                indent=2,
            )
        )
