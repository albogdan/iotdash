from flask import Blueprint

# Create the home Blueprint
dash = Blueprint('dash', __name__, url_prefix='/dash')

from application.dash import controllers
