from __future__ import annotations
import logging
from typing import Any, Self, Union
from discord.ext.commands import Cog, GroupCog, hybrid_command, Context
from discord.app_commands import guilds
from discord.voice_client import VoiceClient
from discord.channel import VoiceChannel
from discord.member import VoiceState
from discord import Member, app_commands, Interaction, User, Message

from ck_bot.cogs.base_cog import BaseCog
from ..utils.constants import CK_GUILD

_log = logging.getLogger(__name__)


class VoiceChannelCog(BaseCog):
    """A Cog for Commands relating to Joining and Leaving Voice Channels in Discord"""

    @app_commands.command(name="join", description="Join voice channel")
    async def join(self, interaction: Interaction) -> None:
        _log.info("")

    @app_commands.command(name="leave", description="Leav voice channel")
    async def leave(self, interaction: Interaction) -> None:
        _log.info("")

    # @hybrid_command(description="Join voice channel(must be in a voice channel)")
    # @guilds(CK_GUILD)
    # async def join(self, ctx: Context) -> None:
    #     # TODO get rid of join and auto-join on play/insert/etc
    #     # TODO Log parameters and more specific relevant data
    #     _log.info("Join called")
    #     if isinstance(ctx.author, Member) and ctx.author.voice is None:
    #         await ctx.reply("You must first join a voice channel", ephemeral=True)
    #     elif (
    #         isinstance(ctx.author, Member)
    #         and isinstance(ctx.author.voice, VoiceState)
    #         and isinstance(ctx.author.voice.channel, VoiceChannel)
    #     ):
    #         _log.info("Joining voice channel {%s}", ctx.author.voice.channel.name)
    #         await ctx.author.voice.channel.connect()

    # @hybrid_command(description="Leave voice channel")
    # @guilds(CK_GUILD)
    # async def quit(self, ctx: Context) -> None:
    #     _log.info("Quit called")
    #     if isinstance(ctx.voice_client, VoiceClient):
    #         await ctx.voice_client.disconnect()
