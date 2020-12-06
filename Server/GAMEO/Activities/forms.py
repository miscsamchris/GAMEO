from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,validators, TextAreaField
class AddActivity(FlaskForm):
    activity_name=StringField("Activity Name",validators=[validators.required()])
    event_name=SelectField(label="Select Event ",choices=[],validators=[validators.required()])
    activity_description=TextAreaField("Description",validators=[validators.required()])
    activity_resources=TextAreaField("Resources",validators=[validators.required()])
    activity_starttime=StringField("Start Time",validators=[validators.required()])
    activity_endtime=StringField("End Time",validators=[validators.required()])
    activity_type=SelectField(label="Activity Type",choices=["Registration","Online","Offline","Quiz"],validators=[validators.required()])
    activity_score=StringField("Score",validators=[validators.required()])
    activity_order=StringField("Order",validators=[validators.required()])
    Voiceover=StringField("Speech Data",validators=[validators.required()])
    submit=SubmitField("Add Activity")

class AddAction(FlaskForm):
    action_name=StringField("Action Name",validators=[validators.required()])
    activity_name=SelectField(label="Select Activity ",choices=[],validators=[validators.required()])
    action_data=TextAreaField("Enter Data required for the Action",validators=[validators.required()])
    action_type=SelectField(label="Action Type",choices=["Question","Register","Form","QR"],validators=[validators.required()])
    action_score=StringField("Action Score",validators=[validators.required()])
    action_order=StringField("Action order",validators=[validators.required()])
    Voiceover=StringField("Speech Data",validators=[validators.required()])
    submit=SubmitField("Add Action")
