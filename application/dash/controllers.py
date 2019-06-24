from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from application.db_models import *

from flask_login import current_user, login_user, logout_user, login_required

# Import the dashboard Blueprint from dash/__init__.py
from application.dash import dash



@dash.route('/', methods=['GET', 'POST'])
@login_required
def index():
    devices = current_user.customer_devices.all()
    cards = list()
    for device in devices:
        temp = {}
        temp['title'] = device.device_name
        temp['body'] = device.device_name
        cards.append(temp)

    #cards = [{"title":"AMAZSING","body":"testasdfadf"},{"title":"AMAZSING","body":"testasdfadf"},{"title":"AMAZSING","body":"testasdfadf"},{"title":"AMAZSING","body":"testasdfadf"},{"title":"AMAZSING","body":"testasdfadf"},{"title":"AMAZSING","body":"testasdfadf"},{"title":"AMAZSING","body":"testasdfadf"},{"title":"AMAZSING","body":"testasdfadf"},{"title":"AMAZSING","body":"testasdfadf"},{"title":"AMAZSING","body":"testasdfadf"}]
    return render_template('dash/index.html', cards=cards)
