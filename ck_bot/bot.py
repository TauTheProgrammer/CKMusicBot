import logging
from typing import Any
from discord.ext.commands.bot import Bot, Context
from discord import AppInfo, Intents
from .utils.color_formatter import ColorFormatter
from .utils.constants import CK_GUILD, CK_BOT_CHANNEL_ID, CONFIG
from .cogs.voice_channel_cog import VoiceChannelCog
from .cogs.music_cog import MusicCog

_log = logging.getLogger(__name__)


class DiscordBot(Bot):
    __instance = None
    __synced: bool = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DiscordBot, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        intents = Intents(
            guilds=True,
            guild_messages=True,
            message_content=True,
            voice_states=True,
            members=True,
        )
        super(DiscordBot, self).__init__(
            command_prefix="/", intents=intents, enable_debug_events=True
        )
        self.check(self.is_command_in_bot_channel)

    async def on_ready(self) -> None:
        if len(self.cogs.values()) == 0:
            await self.add_cog(VoiceChannelCog(self), guild=CK_GUILD)
            await self.add_cog(MusicCog(self), guild=CK_GUILD)

        # TODO: Optimize cache
        _log.info("Logged on as %s", self.user)
        await self.ensure_application_configuration()
        await self.wait_until_ready()
        if CONFIG.SHOULD_SYNC_COMMANDS == "1" and not self.__synced:
            _log.info("Syncing commands")
            await self.tree.sync(guild=CK_GUILD)
            self.__synced = True

    def dispatch(self, event_name: str, /, *args: Any, **kwargs: Any) -> None:
        # if (
        #     event_name == "command"
        #     and args
        #     and isinstance(args[0], Context)
        #     and isinstance(args[0].interaction, Interaction)
        # ):
        # TODO: log command names and arguments/values
        if event_name == "interaction":
            _log.info("")
        super().dispatch(event_name, *args, **kwargs)

    def run(self):
        super().run(
            CONFIG.DISCORD_CLIENT_TOKEN,
            log_handler=logging.StreamHandler(),
            log_formatter=ColorFormatter(),
            log_level=logging.DEBUG,
        )

    async def ensure_application_configuration(self) -> None:
        # TODO: Properly verify all flags are exactly as they should be
        application_info: AppInfo = await self.application_info()
        if (
            application_info.flags.gateway_guild_members_limited is False
            or application_info.flags.gateway_message_content_limited is False
        ):
            _log.error("Discord App not configured for message content")

    async def is_command_in_bot_channel(self, ctx: Context) -> bool:
        is_command_in_bot_channel: bool = ctx.channel.id == CK_BOT_CHANNEL_ID
        if not is_command_in_bot_channel:
            await ctx.send("Please enter command in bot channel", ephemeral=True)
        return is_command_in_bot_channel
