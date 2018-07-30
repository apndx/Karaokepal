from application import app, db
from flask import redirect, render_template, request, url_for
from application.songs.models import Song

@app.route("/songs", methods=["GET"])
def songs_index():
    return render_template("songs/list.html", songs = Song.query.all())

@app.route("/songs/new/")
def songs_form():
    return render_template("songs/new.html")

@app.route("/songs/<song_id>/", methods=["GET"])
def songs_change_name(song_id):

    t = Song.query.get(song_id)
    
    return render_template("songs/change.html", t=t)

@app.route("/songs/<song_id>",  methods=["POST"])
def change_form(song_id):

    t = Song.query.get(song_id)   
    t.name = request.form.get("name")
    db.session().commit()
    return redirect(url_for("songs_index"))

@app.route("/songs/", methods=["POST"])
def songs_create():
    t = Song(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("songs_index"))
