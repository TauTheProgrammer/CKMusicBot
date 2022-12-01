import logging
from discord.utils import _ColourFormatter
from ck_bot.utils.constants import CONFIG


class ColorFormatter(logging.Formatter):
    LEVEL_COLOURS = [
        (logging.DEBUG, "\x1b[40;1m"),
        (logging.INFO, "\x1b[34;1m"),
        (logging.WARNING, "\x1b[33;1m"),
        (logging.ERROR, "\x1b[31m"),
        (logging.CRITICAL, "\x1b[41m"),
    ]
    FORMAT = {
        level: logging.Formatter(
            f"\x1b[30;1m%(asctime)s\x1b[0m {colour}%(levelname)-8s\x1b[0m \x1b[1;38;5;43m%(name)s\x1b[1;38;5;43m %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )
        for level, colour in LEVEL_COLOURS
    }

    def format(self, record):
        formatter = self.FORMAT.get(record.levelno)
        if formatter is None:
            formatter = self.FORMAT[logging.DEBUG]

        # Override the traceback to always print in red
        if record.exc_info:
            text = formatter.formatException(record.exc_info)
            record.exc_text = f"\x1b[31m{text}\x1b[0m"

        output = formatter.format(record)

        # Remove the cache layer
        record.exc_text = None
        return output


library, _, _ = __name__.partition(".")
ck_logger = logging.getLogger(library)
handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter())
ck_logger.setLevel(CONFIG.LOG_LEVEL_CK)
ck_logger.addHandler(handler)
