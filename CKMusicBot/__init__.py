import logging

from ckmusicbot.utils.color_formatter import ColorFormatter

logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter())
logger.setLevel(logging.NOTSET)
logger.addHandler(handler)
