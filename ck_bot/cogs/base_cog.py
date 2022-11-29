from typing import Any
from discord.ext.commands import Cog
from discord.ext.commands.bot import Bot
from discord import app_commands

from ck_bot.utils.constants import CK_GUILD


@app_commands.guild_only()
@app_commands.guilds(CK_GUILD)
class BaseCog(Cog):
    __instance = None

    def __new__(cls, *args: Any, **kwargs: Any):
        if cls.__instance is None:
            cls.__instance = super(BaseCog, cls).__new__(cls)
        return cls.__instance

    def __init__(self, bot: Bot):
        self._bot = bot
