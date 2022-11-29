from __future__ import annotations
import logging
from typing import Optional, Any
from discord.ext.commands import (
    Cog,
    hybrid_command,
    Context,
    hybrid_group,
    HybridGroup,
    Group,
)
from discord.app_commands import describe, guilds

from ck_bot.cogs.base_cog import BaseCog
from ..utils.constants import CK_GUILD
from ..spotify.client import CKSpotifyClient
from ..spotify.utils import SpotifyQueryBuilder

_log = logging.getLogger(__name__)


class MusicCog(BaseCog):
    def test(self) -> None:
        _log.info("")

    # @hybrid_command(
    #     description="Play a Song, Album, Playlist, Episode, Link, whatever!"
    # )
    # @describe(
    #     track="Track name",
    #     artist="Artist name",
    #     link="Copied link",
    # )
    # @guilds(CK_GUILD)
    # async def play(
    #     self,
    #     ctx: Context,
    #     track: str,
    #     artist: Optional[str],
    #     album: Optional[str],
    #     link: Optional[str],
    # ) -> None:
    #     # TODO: handle link
    #     query_builder: SpotifyQueryBuilder = SpotifyQueryBuilder(track).add_limit(1)
    #     if artist:
    #         query_builder.with_artist(artist)
    #     if album:
    #         query_builder.with_album(album)
    #     self._spotify_client.search(query_builder.build())
    #     _log.info("Play called")

    # @hybrid_command(description="Skip whatever is currently playing")
    # @guilds(CK_GUILD)
    # async def skip(self, ctx: Context) -> None:
    #     _log.info("Skip called")

    # @hybrid_command(description="Insert a song at the top of the queue")
    # @describe(playable="Song, Album, Playlist, Episodes, Links, whatever!")
    # @guilds(CK_GUILD)
    # async def insert(self, ctx: Context, playable: str) -> None:
    #     _log.info("Insert called")

    # @hybrid_command(
    #     description="Undo last command, if it has not already been processed"
    # )
    # @guilds(CK_GUILD)
    # async def undo(self, ctx: Context) -> None:
    #     _log.info("Undo called")
