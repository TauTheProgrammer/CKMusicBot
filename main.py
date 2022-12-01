from ck_bot.bot import DiscordBot
from ck_bot.utils.constants import CONFIG

bot: DiscordBot = DiscordBot()
bot.run(
    CONFIG.DISCORD_CLIENT_TOKEN,
    log_level=CONFIG.LOG_LEVEL_DISCORD,
)
