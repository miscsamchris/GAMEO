from GAMEO import db

class Event(db.Model):
    __tablename__="Events"
    id=db.Column(db.Integer,primary_key=True)
    event_name=db.Column(db.Text,unique=True, nullable=False)
    event_date=db.Column(db.Text, nullable=False)
    event_state=db.Column(db.Text, nullable=False)
    event_description=db.Column(db.Text, nullable=False)
    activities=db.relationship("Activity",backref="Event",primaryjoin="Event.id == Activity.event_id")
    users=db.relationship("User",backref="Event",primaryjoin="Event.id == User.event_id")
    def __init__(self, name,date,description):
        self.event_name=name
        self.event_date=date
        self.event_state="Created"
        self.event_description=description
    def __repr__(self):
        return f"{self.event_name}"

class Activity(db.Model):
    __tablename__="Activities"
    id=db.Column(db.Integer,primary_key=True)
    activity_name=db.Column(db.Text)
    event_id=db.Column(db.Integer,db.ForeignKey("Events.id"))
    activity_description=db.Column(db.Text,nullable=False)
    activity_resources=db.Column(db.Text)
    activity_starttime=db.Column(db.Text)
    activity_endtime=db.Column(db.Text)
    activity_status=db.Column(db.Text)
    activity_order=db.Column(db.Text)
    activity_score=db.Column(db.Text)
    Voiceover=db.Column(db.Text)
    activity_type=db.Column(db.Text,nullable=False)
    actions=db.relationship("Action",backref="Activity",primaryjoin="Activity.id == Action.activity_id")
    def __init__(self, activity_name,event_id,activity_description,activity_resources,activity_type,activity_starttime,activity_endtime,activity_status,activity_order,activity_score,Voiceover):
        self.activity_name=activity_name    
        self.event_id=event_id
        self.activity_description=activity_description
        self.activity_resources=activity_resources
        self.activity_type=activity_type
        self.activity_starttime=activity_starttime
        self.activity_endtime=activity_endtime
        self.activity_status=activity_status
        self.activity_order=activity_order
        self.activity_score=activity_score
        self.Voiceover=Voiceover
    def __repr__(self):
        return f"{self.activity_name}"

class Action(db.Model):
    __tablename__="Actions"
    id=db.Column(db.Integer,primary_key=True)
    action_name=db.Column(db.Text)
    activity_id=db.Column(db.Integer,db.ForeignKey("Activities.id"))
    action_type=db.Column(db.Text)
    action_data=db.Column(db.Text)
    action_status=db.Column(db.Text)
    action_order=db.Column(db.Integer)
    action_score=db.Column(db.Integer)
    Voiceover=db.Column(db.Text)
    def __init__(self, action_name,action_type,activity_id,action_data,action_status,action_order,action_score,Voiceover):
        self.action_name=action_name    
        self.action_type=action_type
        self.activity_id=activity_id
        self.action_data=action_data
        self.action_status=action_status
        self.action_order=action_order
        self.action_score=action_score
        self.Voiceover=Voiceover
    def __repr__(self):
        return f"{self.video_name} : {self.video_path}"
class User(db.Model):
    __tablename__="Users"
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.Text)
    user_adjective=db.Column(db.Text)
    event_id=db.Column(db.Integer,db.ForeignKey("Events.id"))
    manager_email=db.Column(db.Text)
    user_email=db.Column(db.Text)
    user_password=db.Column(db.Text)
    user_score=db.Column(db.Integer)
    def __init__(self,user_email,user_password,manager_email,event_id):
        self.user_email=user_email    
        self.user_password=user_password
        self.user_score=0
        self.manager_email=manager_email
        self.event_id=event_id
    def registeruser(self,user_name,user_adjective,event_name):
        self.user_name=user_name
        self.user_adjective=user_adjective
        leaderentry=Leaderboard(user_name,event_name)
        db.session.add(leaderentry)
        db.session.commit()
    def __repr__(self):
        return f"{self.user_name}"

class ActivityLog(db.Model):
    __tablename__="ActivityLogs"
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.Text)
    user_email=db.Column(db.Text)
    activity_name=db.Column(db.Text)
    action_name=db.Column(db.Integer)
    score_update_value=db.Column(db.Integer)
    def __init__(self,user_name,user_email,activity_name,action_name,score_update_value):
        self.user_name=user_name
        self.user_email=user_email
        self.activity_name=activity_name
        self.action_name=action_name
        self.score_update_value=score_update_value
    def __repr__(self):
        return f"{self.user_name} : {self.score_update_value}"

class Leaderboard(db.Model):
    __tablename__="Leaderboard"
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.Text)
    event_name=db.Column(db.Text)
    user_score=db.Column(db.Integer)
    def __init__(self,user_name,event_name):
        self.user_name=user_name    
        self.user_score=0
        self.event_name=event_name
    def updatescore(user_name,event_name,score):
        user=Leaderboard.query.filter_by(event_name=event_name,user_name=user_name).first()
        if  user != None:
            user.user_score=score
            db.session.commit()
    def __repr__(self):
        return f"{self.user_name}"
