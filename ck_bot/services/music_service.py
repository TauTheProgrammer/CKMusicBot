import logging
import re
from typing import List
from discord import Interaction
from discord.ext.commands import Bot
from discord import VoiceClient, Member, VoiceChannel
from ck_bot.spotify.client import SpotifyClient
from ck_bot.youtube.client import YoutubeClient

_log = logging.getLogger(__name__)


class MusicService:
    # TODO Lazy initialize
    # TODO Uninitialize after inactivity
    __spotify: SpotifyClient = SpotifyClient()
    # TODO Lazy initialize
    # TODO Uninitialize after inactivity
    __youtube: YoutubeClient = YoutubeClient()
    __queue: List = []
    __bot: Bot

    #########################################
    # Constructors
    #########################################
    def __init__(self, bot: Bot):
        self.__bot = bot

    #########################################
    # Getters/Setters
    #########################################
    @property
    def queue_length(self) -> int:
        return len(self.__queue)

    #########################################
    # Public API
    #########################################
    async def play(self, interaction: Interaction, media: str) -> None:
        if not self.__is_bot_in_voice_channel():
            await self.__join(interaction)

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

    async def quit(self, interaction: Interaction) -> None:
        if self.__is_bot_in_voice_channel():
            voice_client: VoiceClient = self.__bot.voice_clients[0]  # type: ignore
            await voice_client.disconnect()
        else:
            await interaction.response.send_message(
                "I am not in a voice channel", ephemeral=True
            )

    #########################################
    # Private Helper Functions
    #########################################
    async def __join(self, interaction: Interaction) -> None:
        member: Member = interaction.user  # type: ignore
        if member.voice is None:
            await interaction.response.send_message(
                "You must first join a voice channel", ephemeral=True
            )
        else:
            voice_channel: VoiceChannel = member.voice.channel  # type: ignore
            await voice_channel.connect()

    def __is_bot_in_voice_channel(self) -> bool:
        return len(self.__bot.voice_clients) != 0
