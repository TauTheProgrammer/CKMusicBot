import logging
from discord import app_commands, Interaction
from ck_bot.cogs.base_cog import BaseCog
from ck_bot.spotify.client import CKSpotifyClient

_log = logging.getLogger(__name__)


class MusicCog(BaseCog):
    @app_commands.command(
        name="play", description="Play a song, album, playlist, or link"
    )
    @app_commands.describe(
        media="name of what you want to play",
    )
    async def play(self, interaction: Interaction, media: str) -> None:
        client = CKSpotifyClient()
        # client.search()

    # @_bot.group()

    # class PlayGroup(app_commands.Group):
    #     pass

    # @PlayGroup.

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
