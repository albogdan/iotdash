#from application import flask_app
#from application.db_models import FroshGroups, Frosh, Admins # import the FroshGroups class from db_models.py
from application import db # import the db instance from application/__init__.py
import click
import os

"""
Encapsulate the commands in a function to be able to register it with the application
and pass different parameters if the need arises
"""
def register(flask_app):
    @flask_app.cli.group()
    def seed():
        """Seeding commands for database tables for frosh groups, etc"""
        pass

    @seed.command()
    def customers():
        """Seeds the Customers table with test customers"""

    @seed.command()
    def devices():
        """Seeds the devices table with test devices"""

    @seed.command()
    def measurements():
        """Seeds the measurements table with test measurements"""
