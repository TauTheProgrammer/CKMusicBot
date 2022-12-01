import logging
from discord.utils import _ColourFormatter
from ck_bot.bot import DiscordBot
from ck_bot.utils.logging_color_formatter import LoggingColorFormatter
from ck_bot.utils.constants import CONFIG


# Root Logger
logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setFormatter(_ColourFormatter())
logger.setLevel(CONFIG.LOG_LEVEL_ROOT)
logger.addHandler(handler)

# CK Logger
ck_logger = logging.getLogger("ck_bot")
ck_logger.propagate = False
ck_handler = logging.StreamHandler()
ck_handler.setFormatter(LoggingColorFormatter())
ck_logger.setLevel(CONFIG.LOG_LEVEL_CK)
ck_logger.addHandler(ck_handler)


bot: DiscordBot = DiscordBot()
bot.run(
    CONFIG.DISCORD_CLIENT_TOKEN,
    log_handler=None,
)
