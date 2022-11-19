from __future__ import annotations
import os
import logging
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy.client import Spotify
from CKMusicBot.utils.types import SpotifyQuery
from ..utils.types import SpotifyQuery

logger = logging.getLogger(__name__)


class CKSpotifyClient(Spotify):
    __instance = None
    __client_id = os.getenv("SPOTIPY_CLIENT_ID")
    __client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    __redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
    __scope = os.getenv("SPOTIPY_SCOPE")
    __username = os.getenv("SPOTIFY_USERNAME")

    @staticmethod
    def get_instance() -> CKSpotifyClient:
        if CKSpotifyClient.__instance is None:
            CKSpotifyClient()
        return CKSpotifyClient.__instance  # type: ignore

    def __init__(self) -> None:
        if CKSpotifyClient.__instance is not None:
            logger.warning(
                "Attempt at additional instantiation of SpotifyClient was made"
            )
        else:
            load_dotenv()
            oauth: SpotifyOAuth = self.__get_auth()
            access_token: str = oauth.get_access_token(as_dict=False)
            # TODO: auth_manager AND client_credentials_manager needed?  They are same thing
            # TODO: Need to ensure with auth_manager that higher rate limit is applied (https://spotipy.readthedocs.io/en/2.21.0/#client-credentials-flow)
            super(CKSpotifyClient, self).__init__(
                auth=access_token,
                auth_manager=self.__get_client_credentials_manager(),
                client_credentials_manager=self.__get_client_credentials_manager(),
                oauth_manager=oauth,
            )
            CKSpotifyClient.__instance = self

    # TODO Investigate using SpotifyPKCE for Authorization Code Flow
    def __get_auth(self) -> SpotifyOAuth:
        return SpotifyOAuth(
            client_id=self.__client_id,
            client_secret=self.__client_secret,
            redirect_uri=self.__redirect_uri,
            scope=self.__scope,
            username=self.__username,
            open_browser=False,
        )

    def __get_client_credentials_manager(self) -> SpotifyClientCredentials:
        return SpotifyClientCredentials(
            client_id=self.__client_id, client_secret=self.__client_secret
        )

    # TODO type the return
    def search(self, query: SpotifyQuery):
        ret = super().search(query.spotify_query, limit=query.limit)
