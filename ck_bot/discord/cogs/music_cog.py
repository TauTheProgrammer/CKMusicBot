from discord import app_commands, Interaction
from discord.ext.commands import Bot

from ...services.music_service import MusicService

from .base.ck_cog import Cog


class MusicCog(Cog):
    __music_service: MusicService

    #########################################
    # Constructors
    #########################################
    def __init__(self, bot: Bot):
        self.__music_service = MusicService(bot)

    #########################################
    # Public API
    #########################################
    # fmt: off
    @app_commands.command(description="Add a song, album, playlist, or link to the queue")
    @app_commands.describe(media="name of what you want to play")
    async def play(self, interaction: Interaction, media: str) -> None:
        await self.__music_service.play(interaction, media)

    @app_commands.command(description="Insert a song into the top of the queue")
    @app_commands.describe(media="name of what you want to insert")
    async def insert(self, interaction: Interaction, media: str) -> None:
        await self.__music_service.insert(interaction, media)

    @app_commands.command(description="Skip current song")
    async def skip(self, interaction: Interaction) -> None:
        self.__music_service.skip(interaction)

    @app_commands.command(description="Clear the queue")
    async def clear(self, interaction: Interaction) -> None:
        self.__music_service.clear(interaction)

    @app_commands.command(description="Leave voice channel")
    async def quit(self, interaction: Interaction) -> None:
        await self.__music_service.quit(interaction)

    # fmt: on

    # TODO Implement Undo?
