class Song:
    count = 0
    artist_count = {}
    genres = []
    artists = []
    genre_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        # Song.count += 1
        # Song.genres.append(self.genre)
   
    @classmethod
    def add_song_to_count(cls):
        cls.count +=1

    @classmethod
    def add_to_genres(cls,genre): #make any name for variable genre
        # cls.genres= list(set(cls.genres))
        # cls.genres.append(genre)
        
        if genre not in cls.genres:
            cls.genres.append(genre)
    
        

    @classmethod
    def add_to_artists(cls, artist):
        # cls.artists= list(set(cls.artists))
        # cls.artists.append(artist)
        if artist not in cls.artists:
            cls.artists.append(artist)
        

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
            
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1



   

# red= Song("barn","beatles","country" )
# ninety= Song("problems","jayZ","Rap" )
# print(ninety.name)
# # print(Song.count)
# print(ninety.count)
# bee= Song("left","Beyonce","RandB" )
# # print(Song.count)
# print(red.genre)