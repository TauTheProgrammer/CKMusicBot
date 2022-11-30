import logging
from discord.voice_client import VoiceClient
from discord.channel import VoiceChannel
from discord import Member, app_commands, Interaction

from ck_bot.cogs.base_cog import BaseCog

_log = logging.getLogger(__name__)


class VoiceChannelCog(BaseCog):
    """A Cog for Commands relating to Joining and Leaving Voice Channels in Discord"""

    @app_commands.command(name="join", description="Join voice channel")
    async def join(self, interaction: Interaction) -> None:
        _log.info("Join called")
        if len(self.bot.voice_clients) == 0:
            member: Member = interaction.user  # type: ignore
            if member.voice is None:
                await interaction.response.send_message(
                    "You must first join a voice channel", ephemeral=True
                )
            else:
                voice_channel: VoiceChannel = member.voice.channel  # type: ignore
                await voice_channel.connect()
        else:
            await interaction.response.send_message(
                "I am already in another voice channel", ephemeral=True
            )

    @app_commands.command(name="leave", description="Leave voice channel")
    async def leave(self, interaction: Interaction) -> None:
        _log.info("Leave called")
        if len(self.bot.voice_clients) != 0:
            voice_client: VoiceClient = self.bot.voice_clients[0]  # type: ignore
            await voice_client.disconnect()
        else:
            await interaction.response.send_message("I am not in a voice channel")
