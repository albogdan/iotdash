from application import db
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
# Import class to create and check password hashes
from werkzeug.security import generate_password_hash, check_password_hash

# Import class to provide functions for login of admins
from flask_login import UserMixin

from application import login_manager
"""
# Commands to initialize a flask database
    # flask db init
        # Creates the migration repository
    # flask db migrate -m "MESSAGE"
        # Adds the models to the migration script (creates the tables)
    # flask db upgrade
        # Upgrades the script to the current migration (adds the new model)
"""
#https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/ - one-to-many relationships tutorial
class Customers(UserMixin, db.Model):
    # Define the columns of the table, including primary keys, unique, and
    # indexed fields, which makes searching faster
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), index=True, nullable=False)
    last_name = db.Column(db.String(255), index=True, nullable=False)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    customer_devices = db.relationship('Devices', backref='devices', lazy='dynamic')
    created_date = db.Column(DateTime(), server_default=func.now()) #func.now() tells the db to calculate the timestamp itself rather than letting the application do it
    updated_date = db.Column(DateTime(), onupdate=func.now())

    # __repr__ method describes how objects of this class are printed
    # (useful for debugging)
    def __repr__(self):
        return '<Customer {}>'.format(self.id) #prints <Customer 'id'>

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_device(self, device):
        if(self.customer_devices.filter(Devices.device_owner == Customers.id).count() > 0):
            self.customer_devices.append(device)

    def remove_device(self, device):
        if(self.customer_devices.filter(Devices.device_owner == Customers.id).count() > 0):
            self.customer_devices.remove(device)


@login_manager.user_loader
def load_user(id):
    return Customers.query.get(int(id))


class Devices(db.Model):
    # Define the columns of the table, including primary keys, unique, and
    # indexed fields, which makes searching faster
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True) #id of the device
    device_name = db.Column(db.String(256), nullable=False)
    device_owner = db.Column(db.Integer, db.ForeignKey('customers.id')) #connect each device to a customer
    device_measurements = db.relationship('Measurements', backref='devices', lazy=True)
    created_date = db.Column(DateTime(), server_default=func.now()) #func.now() tells the db to calculate the timestamp itself rather than letting the application do it
    updated_date = db.Column(DateTime(), onupdate=func.utcnow())

    def __repr__(self):
        return '<Device {}>'.format(self.id) #prints <Device 'id'>


class Measurements(db.Model):
    # Define the columns of the table, including primary keys, unique, and
    # indexed fields, which makes searching faster
    __tablename__ = 'measurements'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256), nullable=False) #name of the measurement, such as temperature, pressure, etc.
    value = db.Column(db.String(256), nullable=False) #value of the measurement
    device = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)
    created_date = db.Column(DateTime(), server_default=func.now()) #time of the measurement
    updated_date = db.Column(DateTime(), onupdate=func.utcnow())

    def __repr__(self):
        return '<Measurement {}>'.format(self.id) #prints <Measurement 'id'>
