import os
from flask import Flask,render_template, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
direc=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(direc,"data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
db=SQLAlchemy(app)
api=Api(app=app)
Migrate(app,db)

from GAMEO.Activities.views import activity_blueprint
from GAMEO.Events.views import event_blueprint
from GAMEO.RestAPI.RESTfulAPI import EventRest,Events,ActivityRest,Activities,UserRest
app.register_blueprint(activity_blueprint,url_prefix="/activity")
app.register_blueprint(event_blueprint,url_prefix="/event")
api.add_resource(EventRest,"/rest/events/<string:name>/")
api.add_resource(Events,"/rest/events/")
api.add_resource(ActivityRest,"/rest/activities/<string:name>/")
api.add_resource(Activities,"/rest/activities/")
api.add_resource(UserRest,"/user/<string:name>/")

