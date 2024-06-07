import discord
from ck_bot.constants import CONFIG

# TODO Move to .env file
CK_GUILD: discord.Object = discord.Object(id=CONFIG.GUILD_ID)
CK_BOT_CHANNEL_ID: int = CONFIG.COMMAND_CHANNEL_ID
