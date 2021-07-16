import click
# from ao3scraper.connection import connection

@click.group()
def fics():
    pass

@fics.command("fics", short_help="help")
@click.option("--commit", "-c", default=False, is_flag=True)
def fics(commit=False):
    if not commit:
        print("Nope")
    get_fics_dude(commit)


def get_fics_dude(commit=False):
    pass
