from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,validators

class AddVideos(FlaskForm):
    Video_name=StringField("Enter the Video Name",validators=[validators.required()])
    Topic_name=SelectField(label="Enter the Topic Name",choices=[],validators=[validators.required()])
    Video_Description=StringField("Enter the Description for the Video",validators=[validators.required()])
    Video_Link=StringField("Enter the Link for the Video",validators=[validators.required(),validators.URL(require_tld=False,message='A valid URL is required.')])
    submit=SubmitField("Add Video")