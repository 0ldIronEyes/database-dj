"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """playlists."""

    __tablename__ = "playlists"
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    songs = db.relationship(
        'Song',
        secondary="playlistsongs",
        backref="playlists",)
    


class Song(db.Model):
    """songs."""
    __tablename__ = "songs"
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    
    __tablename__ = "playlistsongs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), primary_key=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)