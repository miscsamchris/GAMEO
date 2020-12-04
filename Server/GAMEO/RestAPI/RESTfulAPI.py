from flask_restful import Resource, Api
from flask import Blueprint
from GAMEO import db,app
from GAMEO.Models import Event,Activity,Action,User
class EventRest(Resource):
    def get(self,name):
        event=Event.query.filter_by(event_name=name).first()
        if event!= None:
            return {"code":200,"id":event.id,"Event Name":event.event_name,"Event Date":event.event_date,"Event State":event.event_state,"Event Description":event.event_description,"Activities": [{"id":activity.id,"Activity Name":activity.activity_name,"Activity starttime":activity.activity_starttime,"Activity endtime":activity.activity_endtime,"Activity State":activity.activity_status,"Activity Description":activity.activity_description,"Activity Resources":activity.activity_resources,"Activity Order":activity.activity_order,"Activity Score":activity.activity_score,"Activity Type":activity.activity_type,"Voiceover":activity.Voiceover,"Actions": [{"Action ID":i.id, "Action Name":i.action_name,"Action Type":i.action_type, "Action Data":i.action_data,"Action Status":i.action_status, "Action Order":i.action_order,"Action Score":i.action_score,"Voiceover":i.Voiceover} for i in list(activity.actions)]} for activity in list(event.activities)],"Users": [{"User email":i.user_email, "User Name":i.user_name} for i in list(event.users)]}
        return {"code":404,"Message":"No Data Found"},404
class UserRest(Resource):
    def get(self,name):
        user=User.query.filter_by(user_email=name).first()
        if user!= None:
            event=Event.query.filter_by(id=user.event_id).first()
            return {"code":200,"id":user.id,"Event Name":event.event_name}
        return {"code":404,"Message":"No Data Found"},404
class Events(Resource):
    def get(self):
        events=Event.query.all()
        if events!= None:
            EVENTS=[]
            for event in events:
                EVENTS.append({"id":event.id,"Event Name":event.event_name,"Event Date":event.event_date,"Event State":event.event_state,"Event Description":event.event_description,"Activities": [{"Activity ID":i.id, "Activity Name":i.activity_name} for i in list(event.activities)],"Users": [{"User email":i.user_email, "User Name":i.user_name} for i in list(event.users)]})
            return {"code":200,"Events":EVENTS}
        return {"code":404,"Message":"No Data Found"},404
class ActivityRest(Resource):
    def get(self,name):
        activity=Activity.query.filter_by(id=name).first()
        if activity!= None:
            return {"code":200,"id":activity.id,"Activity Name":activity.activity_name,"Activity starttime":activity.activity_starttime,"Activity endtime":activity.activity_endtime,"Activity State":activity.activity_status,"Activity Description":activity.activity_description,"Activity Resources":activity.activity_resources,"Activity Order":activity.activity_order,"Activity Score":activity.activity_score,"Activity Type":activity.activity_type,"Voiceover":activity.Voiceover,"Actions": [{"Action ID":i.id, "Action Name":i.action_name,"Action Type":i.action_type, "Action Data":i.action_data,"Action Status":i.action_status, "Action Order":i.action_order,"Action Score":i.action_score,"Voiceover":i.Voiceover} for i in list(activity.actions)]}
        return {"code":404,"Message":"No Data Found"},404
class Activities(Resource):
    def get(self):
        activities=Activity.query.all()
        if activities!= None:
            ACTIVITIES=[]
            for activity in activities:
                ACTIVITIES.append({"code":200,"id":activity.id,"Activity Name":activity.activity_name,"Activity starttime":activity.activity_starttime,"Activity endtime":activity.activity_endtime,"Activity State":activity.activity_status,"Activity Description":activity.activity_description,"Activity Resources":activity.activity_resources,"Activity Order":activity.activity_order,"Activity Score":activity.activity_score,"Activity Type":activity.activity_type,"Actions": [{"Action ID":i.id, "Action Name":i.action_name,"Action Type":i.action_type, "Action Data":i.action_data,"Action Status":i.action_status, "Action Order":i.action_order,"Action Score":i.action_score} for i in list(activity.actions)]})
            return {"code":200,"Events":ACTIVITIES}
        return {"code":404,"Message":"No Data Found"},404