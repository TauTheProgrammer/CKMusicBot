from enum import Enum
from typing import NamedTuple


class ListEnum(Enum):
    @classmethod
    def to_list(cls):
        return list(map(lambda c: c.value, cls))


class MediaTypes(ListEnum):
    SONG = "track"
    ALBUM = "album"
    PLAYLIST = "playlist"
    LINK = "link"


class SpotifyQuery(NamedTuple):
    spotify_query: str
    spotify_query_type: str
    limit: int


class EnvDict(NamedTuple):
    DISCORD_CLIENT_TOKEN: str
    SHOULD_SYNC_COMMANDS: str
    SPOTIPY_CLIENT_ID: str
    SPOTIPY_CLIENT_SECRET: str
    SPOTIPY_REDIRECT_URI: str
    SPOTIPY_SCOPE: str
    SPOTIFY_USERNAME: str
