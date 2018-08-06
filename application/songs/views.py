from flask import redirect, render_template, request, url_for

from application import app, db
from application.songs.models import Song
from application.songs.forms import SongForm

@app.route("/songs", methods=["GET"])
def songs_index():
    return render_template("songs/list.html", songs = Song.query.all())

@app.route("/songs/new/")
def songs_form():
    return render_template("songs/new.html", form = SongForm())

@app.route("/songs/<song_id>/", methods=["GET"])
def songs_change_name(song_id):

    t = Song.query.get(song_id)
    
    # return render_template("songs/change.html", t=t ) 
    return render_template("songs/change.html", t=t, form = SongForm() )

@app.route("/songs/<song_id>",  methods=["POST"])
def change_form(song_id):

    # t = Song.query.get(song_id)   
    # t.name = request.form.get("name")
    # db.session().commit()
    # return redirect(url_for("songs_index"))

    form = SongForm(request.form)
    t = Song.query.get(song_id) 
    t.name = form.name.data
    t.description = form.description.data
    db.session().commit()
     
    return redirect(url_for("songs_index"))

    #return render_template("songs/change.html", form = SongForm())



@app.route("/songs/", methods=["POST"])
def songs_create():
    form = SongForm(request.form)
    
    if not form.validate():
        return render_template("songs/new.html", form = form)

    t = Song(form.name.data)
    t.description = form.description.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("songs_index"))
