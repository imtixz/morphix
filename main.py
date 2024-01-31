import click

@click.group()
def cli():
    pass

@cli.command()
def init():
    print("This will initiate the project, copy some files into cd")
