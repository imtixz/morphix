import os
import datetime
import importlib

import click

from settings import db

def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    # Capitalize the first letter of each word except the first one
    camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_string

def generate_file_content(name):
    return f"""
from morphix.fields import Column
from morphix.operations import OPERATIONS

class {name}():

    @staticmethod
    def up(db):
        schema = {{
            'id': Column['IntegerField'](),
            'name': Column['VarCharField'](60),
            'marks': Column['FloatField']()
        }}
        OPERATIONS['CREATE_TABLE'](db, 'user', schema)

    @staticmethod
    def down(db):
        OPERATIONS['DROP_TABLE'](db, 'user')

migration = {name}
    """

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def generate(name):
    class_name = snake_to_camel(name)
    file_content = generate_file_content(class_name)

    file_name = f"migrations/{int(datetime.datetime.now().timestamp())}_{name}.py"

    file = open(file_name,"w")
    file.write(file_content)
    file.close()

@cli.command()
def migrate():
    files = sorted(os.listdir('migrations'))
    migrations = []

    for f in files:
        m = importlib.import_module(f'{f[:-3]}')
        m.migration.up()

# TODO: Squash and Rollback commands

if __name__ == '__main__':
    cli()
