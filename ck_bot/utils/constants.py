import discord
from ck_bot.utils.types import EnvDict
from ck_bot.utils.utils import parse_env_file

# Discord
CK_GUILD: discord.Object = discord.Object(id=532945585238441994)
CK_BOT_CHANNEL_ID: int = 755428432921493594

# Env
CONFIG: EnvDict = parse_env_file()
