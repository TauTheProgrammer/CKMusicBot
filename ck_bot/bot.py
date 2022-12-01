import logging
from discord.ext.commands.bot import Bot
from discord import AppInfo, Intents
from .command_tree import BotChannelCommandtree
from .utils.constants import CK_GUILD, CONFIG
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
            command_prefix="/",
            intents=intents,
            enable_debug_events=True,
            tree_cls=BotChannelCommandtree,
        )

    async def on_ready(self) -> None:
        if len(self.cogs.values()) == 0:
            await self.add_cog(MusicCog(self), guild=CK_GUILD)

        # TODO: Optimize cache
        await self.ensure_application_configuration()
        await self.wait_until_ready()
        if CONFIG.SHOULD_SYNC_COMMANDS == "1" and not self.__synced:
            _log.info("Syncing commands")
            await self.tree.sync(guild=CK_GUILD)
            self.__synced = True

    async def ensure_application_configuration(self) -> None:
        # TODO: Properly verify all flags are exactly as they should be
        application_info: AppInfo = await self.application_info()
        if (
            application_info.flags.gateway_guild_members_limited is False
            or application_info.flags.gateway_message_content_limited is False
        ):
            _log.error("Discord App not configured for message content")
