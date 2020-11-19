from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,validators, TextAreaField
class AddActivity(FlaskForm):
    activity_name=StringField("Enter the Activity Name",validators=[validators.required()])
    event_name=SelectField(label="Select the Event ",choices=[],validators=[validators.required()])
    activity_description=TextAreaField("Enter the Description for the Activity",validators=[validators.required()])
    activity_resources=TextAreaField("Enter the Resources given for the Activity. Hyperlinks, Instructions, etc.",validators=[validators.required()])
    activity_starttime=StringField("Enter the Start Time for the Activity",validators=[validators.required()])
    activity_endtime=StringField("Enter the End Time for the Activity",validators=[validators.required()])
    activity_type=SelectField(label="Select the type of the Activity ",choices=["Registration","Online","Offline","Quiz"],validators=[validators.required()])
    activity_score=StringField("Enter the Activity Score",validators=[validators.required()])
    activity_order=StringField("Enter the Activity order",validators=[validators.required()])
    submit=SubmitField("Add Activity")

class AddAction(FlaskForm):
    action_name=StringField("Enter the Action Name",validators=[validators.required()])
    activity_name=SelectField(label="Select the Activity ",choices=[],validators=[validators.required()])
    action_data=TextAreaField("Enter Data required for the Action",validators=[validators.required()])
    action_type=SelectField(label="Select the type of the Action ",choices=["Question","Registration","Form"],validators=[validators.required()])
    action_score=StringField("Enter the Action Score",validators=[validators.required()])
    action_order=StringField("Enter the Action order",validators=[validators.required()])
    submit=SubmitField("Add Action")