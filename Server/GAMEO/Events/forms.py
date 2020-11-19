from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,validators,TextAreaField
from wtforms.fields.html5 import DateField,EmailField

class AddEvent(FlaskForm):
    event_name=StringField("Enter the Event Name",validators=[validators.required()])
    event_description=TextAreaField("Enter the Event Description",validators=[validators.required()])
    event_date=DateField('Choose the event date', format='%Y-%m-%d')
    submit=SubmitField("Add Event")

class AddUser(FlaskForm):
    user_email=EmailField("Enter the User Email",validators=[validators.required()])
    user_password=StringField("Enter the User Password",validators=[validators.required()])
    manager_email=EmailField('Choose the Manager Email')
    submit=SubmitField("Add User")