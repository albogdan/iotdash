from application import db
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
"""
# Commands to initialize a flask database
    # flask db init
        # Creates the migration repository
    # flask db migrate -m "MESSAGE"
        # Adds the models to the migration script (creates the tables)
    # flask db upgrade
        # Upgrades the script to the current migration (adds the new model)
"""

class Users(db.Model):
    # Define the columns of the table, including primary keys, unique, and
    # indexed fields, which makes searching faster
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), index=True)
    last_name = db.Column(db.String(255), index=True)
    discipline = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), index=True, unique=True)
    gender = db.Column(db.String(255))
    signed_in = db.Column(db.Boolean, default=False)
    created_date = db.Column(DateTime(), server_default=func.now()) #func.now() tells the db to calculate the timestamp itself rather than letting the application do it
    updated_date = db.Column(DateTime(), onupdate=func.now())

    downloadable_columns= [('id','ID'), ('first_name','First Name'), ('last_name', 'Last Name'), ('discipline', 'Discipline'), ('email', 'Email'), ('gender', 'Gender'), ('signed_in', 'Signed-In')]
    # __repr__ method describes how objects of this class are printed
    # (useful for debugging)
    def __repr__(self):
        return '<User {}>'.format(self.first_name) #prints <User 'username'>


class FroshGroups(db.Model):
    # Define the columns of the table, including primary keys, unique, and
    # indexed fields, which makes searching faster
    __tablename__ = 'frosh_groups'
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(32), index=True, unique=True)
    facebook_link = db.Column(db.String(128), unique=True)
    created_date = db.Column(DateTime(), server_default=func.now()) #func.now() tells the db to calculate the timestamp itself rather than letting the application do it
    updated_date = db.Column(DateTime(), onupdate=func.utcnow())

    downloadable_columns= [('id','ID'), ('group_name', 'Group Name'), ('facebook_link', 'Facebook Link')]

    def __repr__(self):
        return '<FroshGroup {}>'.format(self.group_name) #prints <FroshGroups 'group_name'>


class Leedurs(db.Model):
    # Define the columns of the table, including primary keys, unique, and
    # indexed fields, which makes searching faster
    __tablename__ = 'leedurs'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), index=True)
    last_name = db.Column(db.String(255), index=True)
    year = db.Column(db.String(255))
    discipline = db.Column(db.String(255))
    email = db.Column(db.String(255), index=True, unique=True)
    phone = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    created_date = db.Column(DateTime(), server_default=func.now()) #func.now() tells the db to calculate the timestamp itself rather than letting the application do it
    updated_date = db.Column(DateTime(), onupdate=func.utcnow())

    downloadable_columns= [id, first_name, last_name, year, discipline, email, phone, gender]

    def __repr__(self):
        return '<FroshGroup {}>'.format(self.group_name) #prints <Leedurs ''>
