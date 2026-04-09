import billboard
from search import SpotifySearch

search = SpotifySearch()

# Billboard.py top 100 songs chart by date
date = input("Which year do you want to travel to? Enter the date in this format: YYYY-MM-DD :")
chart = billboard.ChartData("hot-100", date)
song_uri_list = []

for song in chart:
    artist_id = SpotifySearch.get_artist_id(search, song.artist)
    if artist_id is None:
        continue
    else:
        artist_uri = f"spotify:artist:{artist_id}"
        song_uri = SpotifySearch.get_song_uri(search, song.artist, song.title)
        song_uri_list.append(song_uri)
        print(f"Artist: {song.artist}, Artist URI: {artist_uri}, Song: {song.title}, Song URI: {song_uri}")

print(song_uri_list)