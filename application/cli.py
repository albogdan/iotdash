#from application import flask_app
from application.db_models import FroshGroups, Users # import the FroshGroups class from db_models.py
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
    def froshgroups():
        """Seeds the FroshGroups table with values from FroshGroups.csv in the seeds/ folder"""
        """Note: if get 'unique constraint failed' then you have to clear the table before you seed it"""
        froshgroups_csv_path = 'application/seeds/FroshGroups.csv'#os.path.join(BASE_DIR, 'FroshGroups.csv')
        with open(froshgroups_csv_path, 'r') as froshgroups_csv:
            for i in froshgroups_csv:
                j = i.split(',')
                record = FroshGroups(group_name = j[0], facebook_link = j[1])
                db.session.add(record)
        db.session.commit()
    @seed.command()
    def users():
        """Seeds the Users table with values from Users.csv in the seeds/ folder"""
        users_csv_path = 'application/seeds/Users.csv'#os.path.join(BASE_DIR, 'FroshGroups.csv')
        with open(users_csv_path, 'r') as users_csv:
            for i in users_csv:
                j = i[:-1].split(',')
                record = Users(first_name=j[1], last_name=j[2], discipline=j[3], email=j[4], gender=j[5])
                db.session.add(record)
        db.session.commit()
