from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField('Search:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SelectTableForm(FlaskForm):
    """Form allows user to choose the table from which to select columns from a drop-down list"""
    # Format: ('VALUE RETURNED ON SUBMIT TO SERVER', 'VALUE DISPLAYED TO USER')
    possibleItems = [('', 'Select A Table'), ('FroshGroups', 'Frosh Groups'), ('Users', 'Frosh')]
    table = SelectField('', choices=possibleItems)
    submit = SubmitField('Submit')


class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class ChooseColumnsForm(FlaskForm):
    """Form allows the user to check off which columns of the db they want returned in CSV file"""
    submit = SubmitField('Submit')
    checkboxes = MultiCheckboxField('Columns', choices = [])
