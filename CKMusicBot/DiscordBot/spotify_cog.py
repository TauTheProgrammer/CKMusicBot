from __future__ import annotations
import logging
from typing import Optional, Any
from discord.ext.commands import Cog, hybrid_command, Context
from discord.app_commands import describe, guilds
from ..utils.constants import CK_GUILD
from ..SpotifyClient.client import CKSpotifyClient
from ..SpotifyClient.utils import SpotifyQueryBuilder

_log = logging.getLogger(__name__)


class SpotifyCog(Cog):
    _instance = None
    _spotify_client: CKSpotifyClient

    def __new__(cls, *args: Any, **kwargs: Any):
        if cls._instance is None:
            cls._instance = super(SpotifyCog, cls).__new__(cls)
            cls._spotify_client = CKSpotifyClient()
        return cls._instance

    @hybrid_command(
        description="Play a Song, Album, Playlist, Episode, Link, whatever!"
    )
    @describe(
        artist="Artist name",
        album="Album name",
        track="Track name",
        link="Copied link",
    )
    @guilds(CK_GUILD)
    async def play(
        self,
        ctx: Context,
        track: str,
        artist: Optional[str],
        album: Optional[str],
        link: Optional[str],
    ) -> None:
        # TODO: handle link
        query_builder: SpotifyQueryBuilder = SpotifyQueryBuilder(track).add_limit(1)
        if artist:
            query_builder.with_artist(artist)
        if album:
            query_builder.with_album(album)
        self._spotify_client.search(query_builder.build())
        _log.info("Play called")

    @hybrid_command(description="Skip whatever is currently playing")
    @guilds(CK_GUILD)
    async def skip(self, ctx: Context) -> None:
        _log.info("Skip called")

    @hybrid_command(description="Insert a song at the top of the queue")
    @describe(playable="Song, Album, Playlist, Episodes, Links, whatever!")
    @guilds(CK_GUILD)
    async def insert(self, ctx: Context, playable: str) -> None:
        _log.info("Insert called")

    @hybrid_command(
        description="Undo last command, if it has not already been processed"
    )
    @guilds(CK_GUILD)
    async def undo(self, ctx: Context) -> None:
        _log.info("Undo called")
