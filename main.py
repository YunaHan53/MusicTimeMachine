import billboard
from search import SpotifySearch
from playlist import Playlist

search = SpotifySearch()
playlist = Playlist()

# Billboard.py top 100 songs chart by date
date = input("Which year do you want to travel to? Enter the date in this format: YYYY-MM-DD : ")
chart = billboard.ChartData("hot-100", date)
song_uri_list = []
year = date.split("-")[0]
playlist_name = f"{date} Billboard 100"

for song in chart:
    # print(f"{song.artist} - {song.title}")
    artist_id = SpotifySearch.get_artist_id(search, song.artist)
    if artist_id is None:
        continue
    else:
        artist_uri = f"spotify:artist:{artist_id}"
        song_uri = SpotifySearch.get_song_uri(search, song.title)
        song_uri_list.append(song_uri)
        # print(f"Artist: {song.artist}, Artist URI: {artist_uri}, Song: {song.title}, Song URI: {song_uri}")

# Checks for existing Billboard playlists for current user
playlist_id = None
current_playlist_id = Playlist.get_current_playlists(playlist, playlist_name)

if current_playlist_id is None:
    new_playlist_id = Playlist.create_playlist(playlist, year, playlist_name)
    playlist_id = new_playlist_id
else:
    playlist_id = current_playlist_id

add_songs = Playlist.add_songs_to_playlist(playlist, playlist_id, song_uri_list)
