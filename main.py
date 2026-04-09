import billboard
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

date = input("Which year do you want to travel to? Enter the date in the format YYYY-MM-DD: ")
chart = billboard.ChartData("hot-100", date)
print(chart)

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="user-library-read"))

results = sp.current_user_saved_tracks(limit=5)
print(results)