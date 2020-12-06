from GAMEO import app,db
import os
import pandas as pd
from flask import Blueprint,render_template,redirect,url_for,request
from GAMEO.Models import Event,User,ActivityLog,Leaderboard
from GAMEO.Events.forms import AddEvent,AddUser
event_blueprint=Blueprint("Event",__name__,template_folder="templates",static_folder="static")

@event_blueprint.route("/create", methods=["GET","POST"])
def addevent():
    form = AddEvent()
    if form.validate_on_submit():
        event_name=form.event_name.data
        event_date=form.event_date.data
        event_description=form.event_description.data
        event=Event(event_name,event_date,event_description)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("Activity.addactivity"))
    return render_template("addevent.html",form=form)

@event_blueprint.route("/events", methods=["GET","POST"])
def getevents():
    events=Event.query.all()
    users=User.query.all()
    return render_template("viewevents.html",events=list(events),users=list(users))


@event_blueprint.route("/activate/", methods=["GET","POST"])    
def activate():
    id=int(request.form["event_id"])
    event=Event.query.get(id)
    if event !=  None:
        event.event_state="Activated"
        db.session.commit()
    return redirect(url_for("Event.getevents"))


@event_blueprint.route("/getusers/",methods=["POST"])
def getusers():
    if request.method=="POST":
        id=int(request.form["event_id"])
        user_file = request.files["users_file"]
        if(".xls" in user_file.filename):
            user_df = pd.read_excel(user_file)
        elif(".csv" in user_file.filename):
            user_df = pd.read_csv(user_file)
        for i in range(0,len(user_df)):
            user=User(user_df.iloc[i,0],user_df.iloc[i,1],user_df.iloc[i,2],id)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for("Event.getevents"))


@event_blueprint.route("/users/", methods=["GET","POST"])
def getscores():
    event_name=request.args.get("name")
    scores=Leaderboard.query.filter_by(event_name=event_name).order_by(Leaderboard.user_score.desc()).all()
    return render_template("adduser.html",scores=list(scores))


@event_blueprint.route("/updatescore/", methods=["GET","POST"])
def updatescore():
    if request.args !=None:
        user_name=request.args.get("user_name")
        event_name=request.args.get("event_name")
        score=request.args.get("score")
        Leaderboard.updatescore(user_name,event_name,score)
    return "Success",200


@event_blueprint.route("/registername/", methods=["GET","POST"])
def registername():
    if request.args !=None:
        user_name=request.args.get("user_name")
        event_name=request.args.get("event_name")
        user_id=request.args.get("user_id")
        user_adjective=request.args.get("user_adjective")
        user=User.query.filter_by(id=user_id).first()
        user.registeruser(user_name,user_adjective,event_name)
    return "Success",200
