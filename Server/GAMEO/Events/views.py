from GAMEO import db
from flask import Blueprint,render_template,redirect,url_for,request
from GAMEO.Models import Event,User,ActivityLog
from GAMEO.Events.forms import AddEvent,AddUser
event_blueprint=Blueprint("Event",__name__,template_folder="templates")

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
    return render_template("viewevents.html",events=list(events))
@event_blueprint.route("/activate/", methods=["GET","POST"])    
def activate():
    id=int(request.form["event_id"])
    event=Event.query.get(id)
    if event !=  None:
        event.event_state="Activated"
        db.session.commit()
    return redirect(url_for("Event.getevents"))

@event_blueprint.route("/users/", methods=["GET","POST"])
def addusers():
    form = AddUser()
    if form.validate_on_submit():
        user_email=form.user_email.data
        user_password=form.user_password.data
        manager_email=form.manager_email.data
        event_id=int(request.args.get("id"))
        user=User(user_email,user_password,manager_email,event_id)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("Event.addusers")+"?id="+str(event_id))
    return render_template("adduser.html",form=form)

@event_blueprint.route("/updatescore/", methods=["GET","POST"])
def updatescore():
    if request.args !=None:
        user_name=request.args.get("user_name")
        user_email=request.args.get("user_email")
        activity_name=request.args.get("activity_name")
        action_name=request.args.get("action_name")
        score_update_value=request.args.get("score_update_value")
        al=ActivityLog(user_name,user_email,activity_name,action_name,score_update_value)
        db.session.add(al)
        db.session.commit()
    return "Success",200


@event_blueprint.route("/registername/", methods=["GET","POST"])
def registername():
    if request.args !=None:
        user_name=request.args.get("user_name")
        event_name=request.args.get("event_name")
        user_email=request.args.get("user_email")
        user_adjective=request.args.get("user_adjective")
        user=User.query.filter_by(user_email=user_email).first()
        user.registeruser(user_name,user_adjective,event_name)
    return "Success",200