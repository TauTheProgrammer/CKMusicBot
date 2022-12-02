import re
from typing import Dict, Any
from dotenv import dotenv_values

from .types.env import EnvDict


def parse_env_file() -> EnvDict:
    env_vars: Dict[str, str] = dotenv_values(".env")  # type: ignore
    config: EnvDict = EnvDict(
        LOG_LEVEL_ROOT=int(env_vars["LOG_LEVEL_ROOT"]),
        LOG_LEVEL_CK=int(env_vars["LOG_LEVEL_CK"]),
        DISCORD_CLIENT_TOKEN=env_vars["DISCORD_CLIENT_TOKEN"],
        SHOULD_SYNC_COMMANDS=env_vars["SHOULD_SYNC_COMMANDS"],
        INACTIVITY_TIMEOUT_SECONDS=int(env_vars["INACTIVITY_TIMEOUT_SECONDS"]),
        SPOTIPY_CLIENT_ID=env_vars["SPOTIPY_CLIENT_ID"],
        SPOTIPY_CLIENT_SECRET=env_vars["SPOTIPY_CLIENT_SECRET"],
        SPOTIPY_REDIRECT_URI=env_vars["SPOTIPY_REDIRECT_URI"],
        SPOTIPY_SCOPE=env_vars["SPOTIPY_SCOPE"],
        SPOTIFY_USERNAME=env_vars["SPOTIFY_USERNAME"],
        YOUTUBE_DATA_API_V3_KEY=env_vars["YOUTUBE_DATA_API_V3_KEY"],
        FF_VOICE=int(env_vars["FF_VOICE"]),
    )
    return config


# TODO: Feel like this shouldn't belong here, the url regex related stuff
__SPOTIFY_BASE_URL = "https:\\/\\/open.spotify.com\\/.*"
__SPOTIFY_SINGLE_VIDEO_URL = "https:\/\/www.youtube.com/watch\?v=([a-zA-Z0-9]*)(?!&)"
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
