from __future__ import annotations
import os
import logging
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy.client import Spotify
from ck_bot.utils.types import SpotifyQuery

logger = logging.getLogger(__name__)


class CKSpotifyClient(Spotify):
    _instance = None
    _client_id = os.getenv("SPOTIPY_CLIENT_ID")
    _client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    _redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
    _scope = os.getenv("SPOTIPY_SCOPE")
    _username = os.getenv("SPOTIFY_USERNAME")

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CKSpotifyClient, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
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

    # TODO Investigate using SpotifyPKCE for Authorization Code Flow
    def __get_auth(self) -> SpotifyOAuth:
        return SpotifyOAuth(
            client_id=self._client_id,
            client_secret=self._client_secret,
            redirect_uri=self._redirect_uri,
            scope=self._scope,
            username=self._username,
            open_browser=True,
        )

    def __get_client_credentials_manager(self) -> SpotifyClientCredentials:
        return SpotifyClientCredentials(
            client_id=self._client_id, client_secret=self._client_secret
        )

    # TODO type the return
    def search(self, query: SpotifyQuery):
        ret = super().search(query.spotify_query, limit=query.limit)
