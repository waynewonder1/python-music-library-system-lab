#!/usr/bin/env python3


class Song:
    # Class attributes - shared across all instances
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger all class methods whenever a new song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        '''Increments the total song count by one.'''
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        '''Adds a new genre to the genres list, keeping entries unique.'''
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        '''Adds a new artist to the artists list, keeping entries unique.'''
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        '''Increments the count for a genre, or initializes it to 1 if new.'''
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        '''Increments the count for an artist, or initializes it to 1 if new.'''
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    def __repr__(self):
        return f"Song('{self.name}', '{self.artist}', '{self.genre}')"