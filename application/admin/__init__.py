from flask import Blueprint

# Create the admin Blueprint
admin = Blueprint('admin', __name__, url_prefix='/admin')


from application.admin import controllers
