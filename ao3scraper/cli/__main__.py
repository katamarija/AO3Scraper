import click
from .fics import fics


@click.group()
def cli():
    pass


cli.add_command(fics)

if __name__ == "__main__":
    cli()
