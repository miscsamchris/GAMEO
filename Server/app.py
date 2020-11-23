from GAMEO import app,db,redirect,url_for
@app.route("/")
def home():
    return redirect(url_for("Event.addevent"))
if __name__=="__main__":
    db.create_all()
    app.run(port=80,host="localhost")
