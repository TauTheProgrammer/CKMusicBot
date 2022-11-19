from __future__ import annotations
import os
import logging
from typing import Any, List, Mapping, Self
from discord.ext.commands.bot import Bot, Context
from discord.ext.commands import Cog
from discord.interactions import Interaction
from discord import Message, AppInfo, Intents
from discord.types.interactions import InteractionData
from dotenv import load_dotenv
from CKMusicBot.utils.color_formatter import ColorFormatter
from ..utils.constants import CK_GUILD, CK_BOT_CHANNEL_ID
from .discord_cog import DiscordCog
from .spotify_cog import SpotifyCog

load_dotenv()
_log = logging.getLogger(__name__)


class DiscordBot(Bot):
    _instance = None
    _synced: bool = False

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super(DiscordBot, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        intents = Intents(
            guilds=True,
            guild_messages=True,
            message_content=True,
            voice_states=True,
            members=True,
        )
        cogs: Mapping = {
            "discord_cog": DiscordCog(),
            "spotify_cog": SpotifyCog(),
        }
        super(DiscordBot, self).__init__(
            command_prefix="/", intents=intents, cogs=cogs, enable_debug_events=True
        )
        self.check(self.is_command_in_bot_channel)

    async def on_ready(self) -> None:
        # TODO: Optimize cache
        if len(self.commands) == 1:
            await self.add_cog_commands()
        _log.info("Logged on as %s", self.user)
        await self.ensure_application_configuration()
        await self.wait_until_ready()
        should_sync_commands: str | None = os.getenv("SHOULD_SYNC_COMMANDS")
        if should_sync_commands == "1" and not self._synced:
            _log.info("Syncing commands")
            await self.tree.sync(guild=CK_GUILD)
            self._synced = True

    async def on_message(self, message: Message) -> None:
        _log.info("Message received from {%s}: {%s}", message.author, message.content)
        return await super().on_message(message)

    def dispatch(self, event_name: str, /, *args: Any, **kwargs: Any) -> None:
        if (
            args
            and isinstance(type(args[0]), Context)
            and isinstance(args[0].interaction, Interaction)
            and args[0].interaction.data is not None
        ):
            ctx: Context = args[0]
            # data: InteractionData = args[0].interaction.data
            # _log.info("Command {%s} invoked with args: %s", ctx.command.name, reduce(lambda a, b: a + ", {key}: {value}".format(key: str =b.), data))  # type: ignore

        super().dispatch(event_name, *args, **kwargs)

    def run(self) -> Self:
        client_token: str | None = os.getenv("CLIENT_TOKEN")
        if client_token is None:
            raise TypeError("Discord bot token undefined")
        super().run(
            client_token,
            log_handler=logging.StreamHandler(),
            log_formatter=ColorFormatter(),
            log_level=logging.DEBUG,
        )
        return self

    async def ensure_application_configuration(self) -> None:
        application_info: AppInfo = await self.application_info()
        if (
            application_info.flags.gateway_guild_members_limited is False
            or application_info.flags.gateway_message_content_limited is False
        ):
            _log.error("Discord App not configured for message content")

    async def add_cog_commands(self) -> None:
        cogs: List[Cog] = [DiscordCog(), SpotifyCog()]
        for cog in cogs:
            commands = cog.get_commands()
            for command in commands:
                self.add_command(command)

    async def is_command_in_bot_channel(self, ctx: Context) -> bool:
        is_command_in_bot_channel: bool = ctx.channel.id == CK_BOT_CHANNEL_ID
        if not is_command_in_bot_channel:
            await ctx.send("Please enter command in bot channel", ephemeral=True)
        return is_command_in_bot_channel
