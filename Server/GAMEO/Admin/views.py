from TrainingTool import db
from flask import Blueprint,render_template,redirect,url_for,send_from_directory,flash
from TrainingTool.Models import Topic,Video
from TrainingTool.Videos.forms import AddVideos
from pytube import YouTube
import sys
video_blueprint=Blueprint("Video",__name__,template_folder="templates",static_folder="static")
def VideoDownload(path,filename,url):
    filename=filename.replace(" ","_")
    try: 
        yt = YouTube(url) 
        yt.streams.filter(progressive=True, file_extension='mp4').order_by("resolution").asc().first().download(output_path=path,filename=filename)
        return True
    except: 
        return False
@video_blueprint.route("/add", methods=["GET","POST"])
def addvideo():
    form = AddVideos()
    topics=Topic.query.all()
    choice=[(i.id,i.topic_name) for i in list(topics)]
    form.Topic_name.choices=choice
    if form.is_submitted():
        name=form.Video_name.data
        topic_id=form.Topic_name.data
        desc=form.Video_Description.data
        video_url=form.Video_Link.data
        video=Video(name,topic_id,desc,video_url)
        path=f"{video_blueprint.root_path}/static/Videos/{topic_id}/{name}"
        path=path.replace("\\","/")
        vid=VideoDownload(path,name,video_url)
        if vid:
            vidname=name.replace(" ","_")+".mp4"
            video.video_path=path+"/"+vidname
            db.session.add(video)
            db.session.commit()
        else:
            flash("Enter a proper Youtube URL")
        return redirect(url_for("Video.addvideo"))
    return render_template("addvideo.html",form=form)
@video_blueprint.route("/stream/<int:id>/", methods=["GET","POST"])
def stream(id):
    video=Video.query.get(id)
    paths=str(video.video_path).split("/")
    path="/".join(paths[0:len(paths)-1])
    filename=paths[-1]
    return send_from_directory(path,filename, as_attachment=True)
