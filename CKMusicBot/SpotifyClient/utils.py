from __future__ import annotations
from CKMusicBot.utils.types import SpotifyQuery


class SpotifyQueryBuilder:
    __spotify_query: str = ""
    __spotify_query_type: str = "track"
    __limit: int = 10

    def __init__(self, search_str: str) -> None:
        self.__spotify_query += search_str

    def add_limit(self, limit: int) -> SpotifyQueryBuilder:
        self.__limit = limit
        return self

    def with_artist(self, artist: str) -> SpotifyQueryBuilder:
        self.__spotify_query += " artist:" + artist
        return self

    def with_album(self, album: str) -> SpotifyQueryBuilder:
        self.__spotify_query += " album:" + album
        return self

    def with_track(self, track: str) -> SpotifyQueryBuilder:
        self.__spotify_query += " track:" + track
        return self

    def build(self) -> SpotifyQuery:
        return SpotifyQuery(
            spotify_query=self.__spotify_query,
            spotify_query_type=self.__spotify_query_type,
            limit=self.__limit,
        )
