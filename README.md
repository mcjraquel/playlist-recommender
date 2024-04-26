# Playlist Recommender

This is a simple app to generate a playlist based on a text prompt given by the user.

## Tools Used

1. Python ([FastAPI](https://fastapi.tiangolo.com/tutorial/)): Language and framework used for the API and Weaviate client
2. [Weaviate](https://weaviate.io/): Vector database to store the Spotify track data
3. [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/): Package used to access Spotify track and playlist data
4. [lyrics.ovh](https://lyricsovh.docs.apiary.io/#): API to fetch lyrics of songs
5. [Docker](https://www.docker.com/): Containerization tool used to instantiate Weaviate
6. [OpenAI API](https://platform.openai.com/docs/overview): API used to vectorize track data into the Weaviate database

## How to use this repo

1. `git clone` this repo using the HTTP link
2. `cd` into the repository folder
3. Create a virtual environment:
   **Windows**:

    ```
    py -3 -m venv venv
    venv\Scripts\activate
    ```

    **macOS/Linux**:

    ```
    python3 -m venv venv
    . venv/bin/activate
    ```

    _Note: Whenever you run this project, you need to activate the virtual environment first._

4. Install the dependencies using the following command:
    ```
    pip install -r requirements.txt
    ```
5. Run the Weaviate Docker instance with the command:
    ```
    docker compose up -d
    ```
6. Create the `Song` Weaviate collection by running the `song.py` script inside the `db.models` folder.
7. Populate the Weaviate database by running the `spotify.py` script.
8. Duplicate the `.env.sample` file and rename it to `.env`. Update it with the correct details.
9. Run the application with the command:
    ```
    uvicorn main:app --reload
    ```
10. Create a `POST` request to the `/generate-playlist/` route with the following properties:
    ```
    {
        "prompt": <ENTER PROMPT HERE>
    }
    ```

## Recommendations

1. For more varied results, try to import more tracks from playlists. One way is to import playlists from Spotify datasets available online.

## Feedback

Thanks for checking out my project! If you have comments feel free to reach out.
