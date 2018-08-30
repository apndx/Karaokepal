# application/songs/views.py

from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.songs.models import Song, Accountsongs
from application.songs.forms import SongForm, ChangeSongForm
from application.artists.models import Artist

@app.route("/songs", methods=["GET"])
def songs_index():
    return render_template("songs/list.html", songs = Song.query.order_by(Song.songname).all())

@app.route("/songs/new/")
@login_required(role="ANY")
def songs_form():
    return render_template("songs/new.html", form = SongForm(), song_error="")

@app.route("/songs/<song_id>/", methods=["GET"])
@login_required()
def songs_change_name(song_id):

    song = Song.query.get(song_id)
    artist_id = Song.find_artist_for_song(song)
    artist = Artist.query.get(artist_id)
    form = ChangeSongForm(obj=song) #the form prefilled with the song

    if not form.validate():
        return render_template("songs/change.html", song=song, artist = artist, form=form)

    return render_template("songs/change.html", song=song, artist = artist, form = SongForm(obj=song) )

@app.route("/songs/<song_id>",  methods=["POST"])
@login_required(role="ANY")
def change_form(song_id):
    song = Song.query.get(song_id) 
    artist_id = Song.find_artist_for_song(song)
    artist = Artist.query.get(artist_id)
    form = ChangeSongForm(obj=song) #the form prefilled with the song 
    
    if not form.validate():
        return render_template("songs/change.html", form = form, song=song, artist=artist, song_error="")

    song.songname = form.songname.data
    song.description = form.description.data
    db.session().commit()
     
    return redirect(url_for("songs_index"))

@app.route("/songs/", methods=["POST"])
@login_required(role="ANY")
def songs_create():
    form = SongForm(request.form)
    
    if not form.validate():
        return render_template("songs/new.html", form = form, song_error="")

    song = Song.query.filter_by(songname=form.songname.data).first()
    artist = Artist.query.filter_by(artistname=form.artistname.data).first()

    if song and artist:
        artistsong = Song.check_artistsong(song, artist)
        print(artistsong)
        if artistsong:
            return render_template("songs/new.html", form = form,    
                                    song_error = "This song has been added already")

        else:
            song = Song(form.songname.data)
            
            db.session().add(song)
            db.session().commit()
            db.session().add(artist)
            db.session().commit()
            song.artists.append(artist) # attach artist and song
            db.session().commit()

            return redirect(url_for("songs_index"))  

    elif song:
        song = Song(form.songname.data)
        song.description = form.description.data

        artist = Artist(form.artistname.data)

        db.session().add(song)
        db.session().commit()
        db.session().add(artist)
        db.session().commit()
        
        song.artists.append(artist) # attach artist and song
        db.session().commit()

        return redirect(url_for("songs_index"))
            
    elif not song:

        song = Song(form.songname.data)
        song.description = form.description.data

        if artist: 
            db.session().add(song)
            db.session().commit()
            db.session().add(artist)
            db.session().commit()
            song.artists.append(artist) # attach artist and song
            db.session().commit()

            return redirect(url_for("songs_index"))

        if not artist:

            artist = Artist(form.artistname.data)

            db.session().add(song)
            db.session().commit()
            db.session().add(artist)
            db.session().commit()
            
            song.artists.append(artist) # attach artist and song
            db.session().commit()

            return redirect(url_for("songs_index"))
    
    return redirect(url_for("songs_index"))

@app.route("/songs/<song_id>/delete/", methods=["POST"])
@login_required(role="ANY")
def song_delete(song_id):

    song = Song.query.get(song_id)
    db.session().delete(song)
    db.session().commit()

    return redirect(url_for("songs_index"))

@app.route("/songs/<song_id>/add/", methods=["GET", "POST"])
@login_required(role="ANY")
def song_choose(song_id):

    song = Song.query.get(song_id)
    form = SongForm(request.form)

    accountsong  = Accountsongs.check_if_exists(song, current_user)
   
    if accountsong:
        return render_template("songs/mylist.html", form = form, mysongs= Song.find_songs_for_current_user(), song_error = "You have this song on your list already")
    
    if not accountsong:    
        accountsong = Accountsongs(current_user, song, 0, 0)
    
        db.session().add(accountsong)
        db.session().commit()

    return redirect(url_for("show_mylist"))

@app.route("/songs/mylist/", methods=["GET"])    
@login_required(role="ANY")
def show_mylist():

    return render_template("songs/mylist.html", mysongs= Song.find_songs_for_current_user(), form = SongForm())

@app.route("/songs/mylist/",  methods=["POST"])     
@login_required(role="ANY")
def mylist_form():

    return redirect(url_for("songs_index")) 

@app.route("/songs/mylist/<song_id>", methods=["POST"]) 
@login_required(role="ANY")
def sing_song(song_id):
    
    accountsong = Accountsongs.query.filter_by(song_id=song_id, account_id =current_user.id).first()
    accountsong.count = accountsong.count + 1 
    db.session().commit()

    return redirect(url_for("show_mylist"))
    
@app.route("/songs/stats/", methods=["GET"]) 
def show_stats():

     return render_template("songs/stats.html", stat_songs = Song.how_many_have_this(), form = SongForm())

@app.route("/songs/stats/", methods=["POST"])   
def songs_stats():

    return redirect(url_for("songs_index")) 