import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

class SpotifySearch:
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_SECRET')
        self.redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= self.client_id,
                                                            client_secret= self.client_secret,
                                                            redirect_uri= self.redirect_uri,
                                                            scope="user-library-read"))

    def get_artist_id(self,artist_name):
        artist_search = self.sp.search(q=f"artist:{artist_name}", type="artist", limit=1)
        items = artist_search["artists"]["items"]
        if not items:
            print(f"Artist {artist_name} not found")
            return None

        artist_id = items[0]["id"]
        return artist_id

    def get_song_uri(self, song_name):
        song_search = self.sp.search(q=f"track:{song_name}", type="track")
        items = song_search["tracks"]["items"]
        if not items:
            print(f"Song {song_name} not found")
            return None

        # artist = items[0]["album"]["artists"][0]["name"]
        # song = items[0]["name"]
        # print(f"Artist: {artist}, Song: {song}")

        song_uri = items[0]["uri"]
        return song_uri
