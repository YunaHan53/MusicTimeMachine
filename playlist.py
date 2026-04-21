import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

class Playlist:
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_SECRET')
        self.redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= self.client_id,
                                                            client_secret= self.client_secret,
                                                            redirect_uri= self.redirect_uri,
                                                            scope="playlist-read-private playlist-modify-private playlist-modify-public "))

    def get_current_playlists(self, pl_name):
        playlists = self.sp.current_user_playlists()
        current_playlists = [playlist for playlist in playlists['items'] if playlist['name'] == pl_name]
        if not current_playlists:
            print("No Billboard playlists found")
            return None
        else:
            name = current_playlists[0]['name']
            return name

    def create_playlist(self, year, pl_name):
        new_playlist = self.sp.current_user_playlist_create(
            name=pl_name,
            public=False,
            collaborative=False,
            description=f"Top 100 songs from {year}")
        playlist_id = new_playlist.get("id")
        print(f"Playlist created: {playlist_id}")
        return playlist_id