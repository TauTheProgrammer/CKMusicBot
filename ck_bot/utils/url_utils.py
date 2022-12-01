import re
from typing import Any

__SPOTIFY_BASE_URL = "https:\\/\\/open.spotify.com\\/.*"
__SPOTIFY_URL = "https:\\/\\/open.spotify.com\\/(track|album|playlist)\\/(.+?(?=\\?))"
__YOUTUBE_BASE_URL = "https:\\/\\/www.youtube.com\\/.*"


def is_spotify_link(media: str) -> bool:
    return re.search(__SPOTIFY_BASE_URL, media) is not None


def is_youtube_link(media: str) -> bool:
    return re.search(__YOUTUBE_BASE_URL, media) is not None


def get_spotify_link_identifiers(media: str) -> tuple[str | Any, ...]:
    results = re.search(__SPOTIFY_URL, media)
    if results is None:
        raise KeyError("Failed to match")
    return results.groups()
