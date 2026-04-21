import billboard
from search import SpotifySearch
from playlist import Playlist

search = SpotifySearch()
playlist = Playlist()

# Billboard.py top 100 songs chart by date
date = input("Which year do you want to travel to? Enter the date in this format: YYYY-MM-DD :")
chart = billboard.ChartData("hot-100", date)
song_uri_list = []
year = date.split("-")[0]
playlist_name = f"Billboard Playlist Year {year}"

for song in chart:
    # print(f"{song.artist} - {song.title}")
    artist_id = SpotifySearch.get_artist_id(search, song.artist)
    if artist_id is None:
        continue
    else:
        artist_uri = f"spotify:artist:{artist_id}"
        song_uri = SpotifySearch.get_song_uri(search, song.title)
        song_uri_list.append(song_uri)
        print(f"Artist: {song.artist}, Artist URI: {artist_uri}, Song: {song.title}, Song URI: {song_uri}")

# Checks for existing Billboard playlists for current user
current_playlists = Playlist.get_current_playlists(playlist, playlist_name)
print(current_playlists)
if current_playlists is None:
    create_pl = Playlist.create_playlist(playlist, year, playlist_name)