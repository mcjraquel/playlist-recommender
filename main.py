import weaviate
import os
from dotenv import load_dotenv

from fastapi import FastAPI
from pydantic import BaseModel
from weaviate.classes.query import MetadataQuery

app = FastAPI()

load_dotenv()


class PlaylistPrompt(BaseModel):
    prompt: str


@app.get("/")
async def root():
    return {
        "message": "App is running! Go to /generate-playlist to generate a playlist based on text prompt."
    }


@app.post("/generate-playlist/")
async def generate_playlist(playlist_prompt: PlaylistPrompt):
    weaviate_client = weaviate.connect_to_local(
        headers={
            "X-OpenAI-Api-Key": os.environ.get("OPENAI_API_KEY"),
        }
    )
    songs = weaviate_client.collections.get("Song")
    similar_songs_response = songs.query.near_text(
        query=playlist_prompt.prompt,
        limit=10,
        return_metadata=MetadataQuery(distance=True),
    )
    weaviate_client.close()

    similar_songs: list = []
    for song in similar_songs_response.objects:
        similar_songs.append(
            {
                "title": song.properties.get("title"),
                "artist": song.properties.get("artist"),
                "lyrics": song.properties.get("lyrics"),
                "acousticness": song.properties.get("acousticness"),
                "danceability": song.properties.get("danceability"),
                "duration_ms": song.properties.get("duration_ms"),
                "energy": song.properties.get("energy"),
                "instrumentalness": song.properties.get("instrumentalness"),
                "liveness": song.properties.get("liveness"),
                "loudness": song.properties.get("loudness"),
                "mode": song.properties.get("mode"),
                "speechiness": song.properties.get("speechiness"),
                "tempo": song.properties.get("tempo"),
                "valence": song.properties.get("valence"),
            }
        )

    return {
        "prompt": playlist_prompt.prompt,
        "similar_songs": similar_songs,
    }
