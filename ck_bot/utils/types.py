from enum import Enum
from typing import NamedTuple


class ListEnum(Enum):
    @classmethod
    def to_list(cls):
        return list(map(lambda c: c.value, cls))


class MediaTypes(ListEnum):
    TRACK = "track"
    ALBUM = "album"
    PLAYLIST = "playlist"
    LINK = "link"


class SpotifyQuery(NamedTuple):
    spotify_query: str
    spotify_query_type: str
    limit: int


class EnvDict(NamedTuple):
    LOG_LEVEL_ROOT: int
    LOG_LEVEL_CK: int
    LOG_LEVEL_DISCORD: int
    DISCORD_CLIENT_TOKEN: str
    SHOULD_SYNC_COMMANDS: str
    INACTIVITY_TIMEOUT_SECONDS: int
    SPOTIPY_CLIENT_ID: str
    SPOTIPY_CLIENT_SECRET: str
    SPOTIPY_REDIRECT_URI: str
    SPOTIPY_SCOPE: str
    SPOTIFY_USERNAME: str
    FF_VOICE: int
