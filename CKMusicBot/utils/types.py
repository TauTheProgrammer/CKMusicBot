from enum import Enum
from typing import NamedTuple


class ListEnum(Enum):
    @classmethod
    def to_list(cls):
        return list(map(lambda c: c.value, cls))


class MediaType(ListEnum):
    ALBUM = "album"
    ARTIST = "artist"
    PLAYLIST = "playlist"
    TRACK = "track"
    SHOW = "show"
    EPISODE = "episode"
    AUDIOBOOK = "audiobook"


class SpotifyQuery(NamedTuple):
    spotify_query: str
    spotify_query_type: str
    limit: int
