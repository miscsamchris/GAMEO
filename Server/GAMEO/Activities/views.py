from GAMEO import db
from flask import Blueprint,render_template,redirect,url_for
from GAMEO.Models import Event,Activity,Action
from GAMEO.Activities.forms import AddActivity,AddAction
activity_blueprint=Blueprint("Activity",__name__,template_folder="templates",static_folder="static")
@activity_blueprint.route("/create", methods=["GET","POST"])
def addactivity():
    form = AddActivity()
    events=Event.query.all()
    choice=[(i.id,i.event_name) for i in list(events)][::-1]
    form.event_name.choices=choice
    if form.is_submitted():
        activity_name=form.activity_name.data
        event_name=form.event_name.data
        activity_description=form.activity_description.data
        activity_resources=form.activity_resources.data
        activity_starttime=form.activity_starttime.data
        activity_endtime=form.activity_endtime.data
        activity_type=form.activity_type.data
        activity_score=form.activity_score.data
        activity_order=form.activity_order.data
        Voiceover=form.Voiceover.data
        activity=Activity(activity_name,event_name,activity_description,activity_resources,activity_type,activity_starttime,activity_endtime,"Created",activity_order,activity_score,Voiceover)
        db.session.add(activity)
        db.session.commit()
        return redirect(url_for("Activity.addaction"))
    return render_template("addactivity.html",form=form)
@activity_blueprint.route("/action/create", methods=["GET","POST"])
def addaction():
    form = AddAction()
    activities=Activity.query.all()
    choice=[(i.id,i.activity_name) for i in list(activities)][::-1]
    form.activity_name.choices=choice
    if form.is_submitted():
        action_name=form.action_name.data
        activity_name=form.activity_name.data
        action_data=form.action_data.data
        action_type=form.action_type.data
        action_score=form.action_score.data
        action_order=form.action_order.data
        Voiceover=form.Voiceover.data
        action=Action(action_name,action_type,activity_name,action_data,"Created",action_order,action_score,Voiceover)
        db.session.add(action)
        db.session.commit()
        return redirect(url_for("Activity.addactivity"))
    return render_template("addaction.html",form=form)