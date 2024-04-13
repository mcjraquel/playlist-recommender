import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import requests

load_dotenv()
client_credentials_manager = SpotifyClientCredentials(client_id=os.environ.get("SPOTIFY_CLIENT_ID"), client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"))
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

for track in sp.playlist_tracks("spotify:playlist:37i9dQZF1DXcBWIGoYBM5M")['items']:
    track_title = track['track']['name']
    track_artist = track['track']['artists'][0]['name']

    try:
        lyrics = requests.get(f"https://api.lyrics.ovh/v1/{track_artist}/{track_title}").json()['lyrics']
        lyrics_wo_title = "\n".join(lyrics.split("\n")[1:])
        print(lyrics_wo_title)
        break
    except KeyError:
        print(f"Lyrics not found for {track_title} by {track_artist}")