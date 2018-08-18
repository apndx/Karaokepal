from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.songs.models import Song
from application.songs.forms import SongForm
from application.artists.models import Artist

@app.route("/songs", methods=["GET"])
def songs_index():
    return render_template("songs/list.html", songs = Song.query.all())

@app.route("/songs/new/")
@login_required
def songs_form():
    return render_template("songs/new.html", form = SongForm())

@app.route("/songs/<song_id>/", methods=["GET"])
@login_required
def songs_change_name(song_id):

    song = Song.query.get(song_id)
    
    return render_template("songs/change.html", song=song, form = SongForm() )

@app.route("/songs/<song_id>",  methods=["POST"])
@login_required
def change_form(song_id):
    song = Song.query.get(song_id) 
    form = SongForm(obj=song) #the form will be prefilled with the song 
    
    song.songname = form.songname.data
    song.description = form.description.data
    db.session().commit()
     
    return redirect(url_for("songs_index"))

@app.route("/songs/", methods=["POST"])
@login_required
def songs_create():
    form = SongForm(request.form)
    
    if not form.validate():
        return render_template("songs/new.html", form = form)

    song = Song(form.songname.data)
    song.description = form.description.data

    artist = Artist.query.filter_by(artistname=form.artistname.data).first()
    if not artist:
        
        artist = Artist(form.artistname.data)

    db.session().add(song)
    db.session().commit()

    db.session().add(artist)
    db.session().commit()
    
    song.artists.append(artist) # attach artist and song
    db.session().commit()
  
    return redirect(url_for("songs_index"))

@app.route("/songs/<song_id>/delete/", methods=["POST"])
@login_required
def song_delete(song_id):

    song = Song.query.get(song_id)
    db.session().delete(song)
    db.session().commit()

    return redirect(url_for("songs_index"))

@app.route("/songs/<song_id>/add/", methods=["GET", "POST"])
@login_required
def song_choose(song_id):

    song = Song.query.get(song_id)
    song.users.append(current_user) # attach user and song
    db.session().add(song)
    db.session().commit()

    return redirect(url_for("songs_index"))
    #return render_template(url_for("songs/mylist.html"))

@app.route("/songs/mylist/", methods=["GET"])    
@login_required
def show_mylist():

    return render_template("songs/mylist.html", mysongs= Song.find_songs_for_current_user(), form = SongForm())

@app.route("/songs/mylist/",  methods=["POST"])     
@login_required
def mylist_form():

    form = SongForm()
    songs = Song.query.get()
    return redirect(url_for("songs_index")) 

@app.route("/songs/stats/", methods=["GET"]) 
def show_stats():

     return render_template("songs/stats.html", stat_songs = Song.how_many_have_this(), form = SongForm())

@app.route("/songs/stats/", methods=["POST"])   
def songs_stats():

    form = SongForm()
    songs = Song.query.get()
    return redirect(url_for("songs_index")) 
