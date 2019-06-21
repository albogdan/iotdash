#from application import flask_app
from application.db_models import Customers, Devices, Measurements # import the FroshGroups class from db_models.py
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
        #init first customer
        c1 = Customers(first_name="A", last_name="B", email="ab@g.com")
        c1.set_password("test123")
        db.session.add(c1)
        db.session.commit()
        print("setup user 1")

        dList = [Devices(device_name="ESP1", device_owner=c1.id), Devices(device_name="ESP3", device_owner=c1.id), Devices(device_name="Arduino", device_owner=c1.id)]
#        dList = [Devices(device_name="ESP1"), Devices(device_name="ESP3"), Devices(device_name="Arduino")]
        for d in dList:
            print("setting up device X ")
            c1.add_device(d)
            db.session.add(d)
            db.session.commit()

        #init second customer
        c2 = Customers(first_name="C", last_name="D", email="cd@g.com")
        c2.set_password("test123")
        db.session.add(c2)
        db.session.commit()

        dList = [Devices(device_name="Telus", device_owner=c2.id), Devices(device_name="Rogers", device_owner=c2.id), Devices(device_name="Alpha", device_owner=c2.id), Devices(device_name="Beta", device_owner=c2.id),Devices(device_name="Gamma", device_owner=c2.id)]
# dList = [Devices(device_name="Telus"), Devices(device_name="Rogers"), Devices(device_name="Alpha"), Devices(device_name="Beta"),Devices(device_name="Gamma")]
        for e in dList:
            c2.add_device(e)
            db.session.add(e)
            db.session.commit()

        print("User 1 devices: {0}".format(c1.customer_devices.count()))
        print("User 2 devices: {0}".format(c2.customer_devices.count()))
    # @seed.command()
    # def devices():
    #     """Seeds the devices table with test devices"""
    #
    # @seed.command()
    # def measurements():
    #     """Seeds the measurements table with test measurements"""
    #
