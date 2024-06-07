import logging
from typing import List
from discord import Interaction, VoiceClient, Member, VoiceChannel
from discord.ext.commands import Bot

from ..types.singleton import Singleton
from ..constants import CONFIG
from ..youtube.client import YoutubeClient
from .. import utils

from .spotify_query_service import SpotifyQueryService
from .youtube_query_service import YoutubeQueryService

_log = logging.getLogger(__name__)


class MusicService(Singleton):
    # TODO Lazy initialize
    # TODO Uninitialize after inactivity
    __spotify_query_service: SpotifyQueryService = SpotifyQueryService()
    __youtube_query_service: YoutubeQueryService = YoutubeQueryService()
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
        search_results: List[str] | str = await self.__get_search_results(media)
        print(search_results)

    async def insert(self, interaction: Interaction, media: str) -> None:
        search_results: List[str] | str = await self.__get_search_results(media)

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
    async def __get_search_results(self, media: str) -> List[str] | str:
        if not utils.is_youtube_link(media):
            return self.__spotify_query_service.query(media)
        # elif utils.is_youtube_single(media):
        # x: List[str] | str = await self.__youtube.fetch_metadata(media)
        # return await self.__youtube.fetch(x)
        return self.__spotify_query_service.query(media)

    async def __join(self, interaction: Interaction) -> None:
        if CONFIG.VOICE_ENABLED:
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
