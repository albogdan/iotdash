from flask import request, render_template, flash, session, redirect, url_for, jsonify, make_response
from application.db_models import *
from application.auth.forms import RegistrationForm, LoginForm # import the SearchForm, SelectTableForm, ChooseColumnsForm classes from forms.py

# Import the admin Blueprint from admin/__init__.py
from application.auth import auth
from application import db
from sqlalchemy.sql import func
from sqlalchemy.orm import load_only
import json
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

"""
Route + function for the landing page for administration
"""
@auth.route('/', methods=['GET','POST'])
@login_required
def admin_home():
    # Get a list of all the users
    allFrosh = Frosh.query.order_by(Frosh.last_name).all()
    # Get a count of how many Frosh have been signed in to display @ bottom of screen
    number_signed_in = Frosh.query.filter(Frosh.signed_in==True).count()
    # Return the template
    return render_template('auth/admin.html', allFrosh=allFrosh, number_signed_in=number_signed_in)
""" This part was used for search when pressing submit"""
"""    searchForm = SearchForm()
    if(searchForm.validate_on_submit()):
        print("Data: {0}".format(searchForm.search.data))
        # func.lower takes care to make case insensitive
        #groups = FroshGroups.query.filter(func.lower(searchForm.search.data) == func.lower(FroshGroups.group_name))
        users = Users.query.filter(Users.first_name.contains(searchForm.search.data)).limit(20)
        return render_template('admin/admin.html', users=users, form=searchForm)

    return render_template('admin/admin.html', users=users, form=searchForm)
"""

"""
INSERT DESCRIPTION HERE
"""

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if(current_user.is_authenticated):
        return redirect(url_for('home.index'))
    form = LoginForm()
    if(form.validate_on_submit()):
        customer = Customers.query.filter_by(email=form.username.data).first()

        if(customer is None or not customer.check_password(form.password.data)):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))

        login_user(customer, remember=form.remember_me.data)
        next_page = request.args.get('next')

        if(not next_page or url_parse(next_page).netloc != ''):
            next_page = url_for('home.index')

        return redirect(next_page)

    return render_template('auth/login.html', title='Customer Sign-In', form=form)

@auth.route('/logout')
def logout():
    print(current_user.customer_devices.all())
    logout_user()
    return redirect(url_for('home.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if(current_user.is_authenticated):
        return redirect(url_for('home.index'))
    form = RegistrationForm()
    if(form.validate_on_submit()):
        print("Submission successful")
        customer = Customers(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
        customer.set_password(form.password.data)
        db.session.add(customer)
        db.session.commit()
        flash('Congratulations, you have successfully registered!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)

"""
Route + function for the AJAX call coming from admin/admin.html which searches
the database in real time and sends updates back to the page via AJAX calls.

Note that returned values from queries contain characters from all the fields
which the user enters characters into.

@admin.route('/updatetable', methods=['GET','POST'])
@login_required
def updateTable():
    # Get the search parameters from the AJAX call through AJAX (see admin.html)
    search_first_name = request.get_json()['search_first_name']
    search_last_name = request.get_json()['search_last_name']

    # Query the database for those parameters and return all matches
    allFrosh = Frosh.query.filter(
        Frosh.first_name.contains(search_first_name),
        Frosh.last_name.contains(search_last_name)).all()

    # Create a dictionary of all of the matches to return to the webpage thru AJAX
    dict = {}
    dict['num'] = len(allFrosh)
    dict['rows'] = []

    # For all queried users parse them and return the wanted fields thru AJAX
    for singleFrosh in allFrosh:
        # NOTE: Javascript JSON parser in admin.html arranges this in alphabetical
        # order based on key name - make sure to have them in alphabetical order
        # as the same order you want to be displayed on the columns on the site
        tempDict = {
            "id" : singleFrosh.id,
            "afirst_name" : singleFrosh.first_name,
            "blast_name" : singleFrosh.last_name,
            "discipline" : singleFrosh.discipline,
            "email" : singleFrosh.email,
            "gender" : singleFrosh.gender,
            "signed_in" : singleFrosh.signed_in
        }
        dict['rows'].append(tempDict)

    # Return the dictionary
    return jsonify(dict)

"""
