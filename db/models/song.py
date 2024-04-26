import os
import weaviate
from dotenv import load_dotenv

from weaviate.classes import config as wcc

load_dotenv()

client = weaviate.connect_to_local(
    headers={
        "X-OpenAI-Api-Key": os.environ.get("OPENAI_API_KEY"),
    }
)

try:
    client.collections.create(
        name="Song",
        vectorizer_config=wcc.Configure.Vectorizer.text2vec_openai(),
        properties=[
            wcc.Property(
                name="title",
                data_type=wcc.DataType.TEXT,
                tokenization=wcc.Tokenization.LOWERCASE,
            ),
            wcc.Property(
                name="artist",
                data_type=wcc.DataType.TEXT,
                tokenization=wcc.Tokenization.LOWERCASE,
            ),
            wcc.Property(
                name="lyrics",
                data_type=wcc.DataType.TEXT,
                tokenization=wcc.Tokenization.LOWERCASE,
            ),
            wcc.Property(
                name="acousticness",
                data_type=wcc.DataType.NUMBER,
            ),
            wcc.Property(
                name="danceability",
                data_type=wcc.DataType.NUMBER,
            ),
            wcc.Property(
                name="duration_ms",
                data_type=wcc.DataType.NUMBER,
            ),
            wcc.Property(
                name="energy",
                data_type=wcc.DataType.NUMBER,
            ),
            wcc.Property(
                name="instrumentalness",
                data_type=wcc.DataType.NUMBER,
            ),
            wcc.Property(
                name="liveness",
                data_type=wcc.DataType.NUMBER,
            ),
            wcc.Property(
                name="loudness",
                data_type=wcc.DataType.NUMBER,
            ),
            wcc.Property(
                name="mode",
                data_type=wcc.DataType.NUMBER,
            ),
            wcc.Property(
                name="speechiness",
                data_type=wcc.DataType.NUMBER,
            ),
            wcc.Property(
                name="tempo",
                data_type=wcc.DataType.NUMBER,
            ),
            wcc.Property(
                name="valence",
                data_type=wcc.DataType.NUMBER,
            ),
        ],
    )

finally:
    client.close()
