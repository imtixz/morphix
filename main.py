import click

# from .morphix.connection import setup_db
# from .morphix.operations import OPERATIONS
# from .morphix.fields import Column


# db = setup_db('./db')

# def main1():
#     schema = {
#         'id': IntegerField(),
#         'name': VarCharField(60),
#         'marks': FloatField()
#     }

#     create_table(db, 'student', schema)

# def main2():
#     rename_table(db, 'student', 'students')

# def main3():
#     drop_table(db, 'students')

# main1()

@click.group()
def cli():
    pass

@cli.command()
def init():
    print("This will initiate the project")

@cli.command()
@click.argument('name')
def generate(name):
    print("This will generate a migration file named {}".format(name))

@cli.command()
def squash():
    print("This will squash the files into one")

@cli.command()
def migrate():
    print("Applies the migration")