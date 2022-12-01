from discord import app_commands, Interaction
from discord.ext.commands import Bot
from ck_bot.cogs.base_cog import BaseCog
from ck_bot.services.music_service import MusicService


class MusicCog(BaseCog):
    __music_service: MusicService

    def __init__(self, bot: Bot):
        self.__music_service = MusicService(bot)

    # @app_commands.command(name="join", description="Join voice channel")
    # async def join(self, interaction: Interaction) -> None:
    #     # _log.info("Join called")
    #     if len(self.bot.voice_clients) == 0:
    #         member: Member = interaction.user  # type: ignore
    #         if member.voice is None:
    #             await interaction.response.send_message(
    #                 "You must first join a voice channel", ephemeral=True
    #             )
    #         else:
    #             voice_channel: VoiceChannel = member.voice.channel  # type: ignore
    #             await voice_channel.connect()
    #     else:
    #         await interaction.response.send_message(
    #             "I am already in another voice channel", ephemeral=True
    #         )

    # @app_commands.command(name="leave", description="Leave voice channel")
    # async def leave(self, interaction: Interaction) -> None:
    #     # _log.info("Leave called")
    #     if len(self.bot.voice_clients) != 0:
    #         voice_client: VoiceClient = self.bot.voice_clients[0]  # type: ignore
    #         await voice_client.disconnect()
    #     else:
    #         await interaction.response.send_message("I am not in a voice channel")

    @app_commands.command(description="Play a song, album, playlist, or link")
    @app_commands.describe(media="name of what you want to play")
    async def play(self, interaction: Interaction, media: str) -> None:
        self.__music_service.play(interaction, media)

    @app_commands.command(description="Insert a song into the top of the queue")
    @app_commands.describe(media="name of what you want to insert")
    async def insert(self, interaction: Interaction, media: str) -> None:
        self.__music_service.insert(interaction, media)

    @app_commands.command(description="Skip current song")
    async def skip(self, interaction: Interaction) -> None:
        self.__music_service.skip(interaction)

    @app_commands.command(description="Clear the queue")
    async def clear(self, interaction: Interaction) -> None:
        self.__music_service.clear(interaction)

    # TODO Implement Undo?
