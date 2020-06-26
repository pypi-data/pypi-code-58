import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('findStatusById')
@click.argument("id_number")
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number):
    """TODO: Undocumented

Output:

    ???
    """
    return ctx.gi.status.findStatusById(id_number)
