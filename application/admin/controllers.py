from flask import request, render_template, flash, session, redirect, url_for, jsonify
from application.db_models import *
from application.admin.forms import SearchForm, SelectTableForm, ChooseColumnsForm # import the SearchForm, SelectTableForm, ChooseColumnsForm classes from forms.py
from application.admin.forms import MultiCheckboxField
# Import the admin Blueprint from admin/__init__.py
from application.admin import admin
from application import db
from sqlalchemy.sql import func
from sqlalchemy.orm import load_only


@admin.route('/', methods=['GET','POST'])
def admin_home():
    users = Users.query.order_by(Users.last_name).all()
    number_signed_in = Users.query.filter(Users.signed_in==True).count()
    return render_template('admin/admin.html', users=users, number_signed_in=number_signed_in)
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

@admin.route('/updatetable', methods=['GET','POST'])
def updateTable():
    search_first_name = request.get_json()['search_first_name']
    search_last_name = request.get_json()['search_last_name']
    users = Users.query.filter(
        Users.first_name.contains(search_first_name),
        Users.last_name.contains(search_last_name)).limit(20).all()

    dict = {}
    dict['num'] = len(users)
    dict['rows'] = []
    print(users)
    for user in users:
        # NOTE: Javascript JSON parser in admin.html arranges this in alphabetical
        # order based on key name - make sure to have them in alphabetical order
        # as the same order you want to be displayed on the columns on the site
        tempDict = {
            "id" : user.id,
            "afirst_name" : user.first_name,
            "blast_name" : user.last_name,
            "discipline" : user.discipline,
            "email" : user.email,
            "gender" : user.gender,
            "signed_in" : user.signed_in
        }
        dict['rows'].append(tempDict)
    return jsonify(dict)


@admin.route('/signin/<id>', methods=['GET', 'POST'])
def signinUser(id):
    user = Users.query.filter(Users.id == id).first()
    user.signed_in = True
    db.session.commit()

    users = Users.query.order_by(Users.last_name).all()

    return redirect('/admin')#, users=users)


@admin.route('/servecsv', methods=['GET', 'POST'])
def send_csv_landing():
    tableSelect = SelectTableForm()
#    if(request.method=='POST'):
#        selectedTable = request.form.get('table'))
        #selection=tableSelect.table.data
        # This is ok b/c you are defining the strings and not the user (in admin/forms.py)
#        className = globals()[selectedTable]
        #allColumns = className.downloadable_columns
        #columnSelect = ChooseColumnsForm(allColumns)
        #return render_template('admin/servecsv.html', selectTableForm=tableSelect)#, selectColumnForm = None)
        #return render_template('admin/servecsv.html', selectTableForm=tableSelect, selectColumnForm = columnSelect)
        #users = className.query.options(load_only(*(allColumns))).all()
        #print(className.downloadable_columns)
        #print(users)
    return render_template('admin/servecsv.html', selectTableForm=tableSelect)#, selectColumnForm = None)

@admin.route('/servecsv/columnselect', methods=['GET', 'POST'])
def table_selected():
    tableSelect = SelectTableForm()
    if(tableSelect.validate_on_submit()):
        selection = tableSelect.table.data
        className = globals()[selection]
        allColumns = className.downloadable_columns
        print(allColumns)
        class F(ChooseColumnsForm):
            pass
        setattr(F, 'checkboxes', MultiCheckboxField('Columns', choices=allColumns))
        columnSelect = F()

        return render_template('admin/columnselect.html', selectTableForm=tableSelect, selectColumnForm=columnSelect)#, selectColumnForm = None)


"""
TO DO:
- Frosh Signin (DONE)
- CSV Download
- Frosh Edit Info
- Frosh Manual Registration
"""
