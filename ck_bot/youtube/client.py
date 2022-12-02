import logging
from yt_dlp import YoutubeDL

_log = logging.getLogger(__name__)


class YoutubeClient:
    __instance = None
    # TODO Lazy initialize
    # TODO Close after inactivity
    # TODO Ensure only necessary information is downloaded
    # TODO Put config in .env?
    # TODO Try to make it output to logger
    # TODO Look into 'Available options:'
    __yt_dlp = YoutubeDL()

    #########################################
    # Constructors
    #########################################
    # TODO Optimize cache if it isn't already

    #########################################
    # Public API
    #########################################

    #########################################
    # Private Helper Functions
    #########################################
