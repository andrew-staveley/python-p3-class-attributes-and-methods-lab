class Song:
    count = 0 #Total number of Song objects
    artists = [] #All artists
    genres = [] #All genres
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.count += 1

    def add_to_genres(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count.update({self.genre: 1})

        if (self.genre) in Song.genres:
            pass
        else:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count.update({self.artist: 1})
            
        if (self.artist) in Song.artists:
            pass
        else:
            Song.artists.append(self.artist)