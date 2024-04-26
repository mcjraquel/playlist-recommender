import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import requests
import weaviate
import logging

logging.basicConfig(level=logging.INFO, filename="spotify.log", filemode="w")

load_dotenv()

client_credentials_manager = SpotifyClientCredentials(
    client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
    client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

weaviate_client = weaviate.connect_to_local(
    headers={
        "X-OpenAI-Api-Key": os.environ.get("OPENAI_API_KEY"),
    }
)

songs = weaviate_client.collections.get("Song")

for track in sp.playlist_tracks("spotify:playlist:37i9dQZF1DXcBWIGoYBM5M")["items"]:
    track_title = track["track"]["name"]
    track_artist = track["track"]["artists"][0]["name"]

    try:
        lyrics = requests.get(
            f"https://api.lyrics.ovh/v1/{track_artist}/{track_title}"
        ).json()["lyrics"]
        lyrics_wo_title = "\n".join(lyrics.split("\n")[1:])

        audio_features = sp.audio_features(track["track"]["uri"])[0]

        data = {
            "title": track_title,
            "artist": track_artist,
            "lyrics": lyrics_wo_title,
            "acousticness": audio_features["acousticness"],
            "danceability": audio_features["danceability"],
            "duration_ms": audio_features["duration_ms"],
            "energy": audio_features["energy"],
            "instrumentalness": audio_features["instrumentalness"],
            "liveness": audio_features["liveness"],
            "loudness": audio_features["loudness"],
            "mode": audio_features["mode"],
            "speechiness": audio_features["speechiness"],
            "tempo": audio_features["tempo"],
            "valence": audio_features["valence"],
        }

        uuid = songs.data.insert(data)

        logging.info(f"Inserted {track_title} by {track_artist} with UUID {uuid}")
    except KeyError:
        logging.error(f"Lyrics not found for {track_title} by {track_artist}")

weaviate_client.close()
