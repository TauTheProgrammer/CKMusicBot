import logging
from typing import List
import googleapiclient.discovery

from ..constants import CONFIG
from ..types.singleton import Singleton

from .base.query_service import QueryService

_log = logging.getLogger(__name__)


class YoutubeQueryService(QueryService, Singleton):
    # TODO Lazy initialize
    # TODO Uninitialize after inactivity
    __google_api_client = None

    #########################################
    # Constructors
    #########################################
    def __init__(self) -> None:
        self.__google_api_client = googleapiclient.discovery.build(
            "youtube",
            "v3",
            developerKey=CONFIG.YOUTUBE_DATA_API_V3_KEY,
        )

    #########################################
    # Overrides
    #########################################
    def query(self, media: str) -> List[str] | str:
        _log.info("")
        return ""
