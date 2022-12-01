import logging
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy.client import Spotify
from ck_bot.utils.constants import CONFIG
from ck_bot.utils.types import SpotifyQuery

_log = logging.getLogger(__name__)


class SpotifyClient(Spotify):
    __instance = None
    # TODO: Fix these, they're ugly

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SpotifyClient, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        oauth: SpotifyOAuth = self.__get_auth()
        access_token: str = oauth.get_access_token(as_dict=False)
        # TODO: auth_manager AND client_credentials_manager needed?  They are same thing
        # TODO: Need to ensure with auth_manager that higher rate limit is applied (https://spotipy.readthedocs.io/en/2.21.0/#client-credentials-flow)
        super(SpotifyClient, self).__init__(
            auth=access_token,
            auth_manager=self.__get_client_credentials_manager(),
            client_credentials_manager=self.__get_client_credentials_manager(),
            oauth_manager=oauth,
        )

    # TODO Investigate using SpotifyPKCE for Authorization Code Flow
    def __get_auth(self) -> SpotifyOAuth:
        # TODO Double check all these properties are needed
        return SpotifyOAuth(
            client_id=CONFIG.SPOTIPY_CLIENT_ID,
            client_secret=CONFIG.SPOTIPY_CLIENT_SECRET,
            redirect_uri=CONFIG.SPOTIPY_REDIRECT_URI,
            scope=CONFIG.SPOTIPY_SCOPE,
            username=CONFIG.SPOTIFY_USERNAME,
            open_browser=True,
        )

    def __get_client_credentials_manager(self) -> SpotifyClientCredentials:
        return SpotifyClientCredentials(
            client_id=CONFIG.SPOTIPY_CLIENT_ID,
            client_secret=CONFIG.SPOTIPY_CLIENT_SECRET,
        )

    def process_link(self, link: str) -> str:
        _log.info("")
        return ""

    # TODO type the return
    def search(self, search_str: str) -> str:
        ret = super().search(search_str, type="track", limit=1)
        if isinstance(ret, str):
            return ret
        else:
            return ""  # TODO handle this
