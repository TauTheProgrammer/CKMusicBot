import logging
import re
from typing import List
from discord import Interaction
from discord.ext.commands import Bot
from ck_bot.spotify.client import SpotifyClient
from ck_bot.youtube.client import YoutubeClient

_log = logging.getLogger(__name__)


class MusicService:
    # TODO Lazy initialize
    __spotify: SpotifyClient = SpotifyClient()
    # TODO Lazy initialize
    __youtube: YoutubeClient = YoutubeClient()
    __queue: List = []
    __bot: Bot

    def __init__(self, bot: Bot):
        self.__bot = bot

    @property
    def queue_length(self) -> int:
        return len(self.__queue)

    def play(self, interaction: Interaction, media: str) -> None:
        if re.search(media, "https://open.spotify.com/.*"):
            _log.info("Process spotify link")
            yt_search_str = self.__spotify.process_link(link=media)
        elif re.search(media, "https://www.youtube.com/.*"):
            _log.info("Process YouTube link")
        else:
            _log.info("Process raw text entry")
            yt_search_str = self.__spotify.search(media)

    def insert(self, interaction: Interaction, media: str) -> None:
        # TODO Make this reusable, generic, something to avoid duplication
        if re.search(media, "https://open.spotify.com/.*"):
            _log.info("Process spotify link")
            yt_search_str = self.__spotify.process_link(link=media)
        elif re.search(media, "https://www.youtube.com/.*"):
            _log.info("Process YouTube link")
        else:
            _log.info("Process raw text entry")
            yt_search_str = self.__spotify.search(media)

    def skip(self, interaction: Interaction) -> None:
        _log.info("")

    def clear(self, interaction: Interaction) -> None:
        _log.info("")
