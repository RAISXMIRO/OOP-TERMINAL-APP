import random
import string

class Song:
    def __init__(self, song_id, title, artist, duration, streams):
        self._song_id = str(song_id)
        self._title = str(title)
        self._artist = str(artist)
        self._duration = float(duration)
        self._streams = int(streams)

    def play(self):
        self._streams += 1

    def get_streams(self):
        return self._streams

    @classmethod
    def generate_id(cls):
        characters = string.ascii_letters + string.digits
        random_id = ''.join(random.choice(characters) for _ in range(10))
        return random_id

    @staticmethod
    def is_valid_duration(duration):
        return 0 < duration < 1200

    def __str__(self):
        return f"{self._title} by {self._artist} ({self._duration}s)"

    def __len__(self):
        return int(self._duration)

    def __add__(self, other):
        if not isinstance(other, Song):
            return NotImplemented
        new_id = self._song_id + other._song_id
        new_title = f"{self._title} X {other._title}"
        new_artist = f"{self._artist} feat. {other._artist}"
        new_duration = max(self._duration, other._duration)
        new_streams = self._streams + other._streams
        return Song(new_id, new_title, new_artist, new_duration, new_streams)


class Single(Song):
    def __init__(self, song_id, title, artist, duration, streams, genre):
        super().__init__(song_id, title, artist, duration, streams)
        self._genre = genre

    def __str__(self):
        return f"[SINGLE] {self._title} by {self._artist} ({self._duration}s), genre: {self._genre}"

    def get_genre(self):
        return self._genre

    def set_genre(self, new_genre):
        self._genre = new_genre
        return self._genre


class LiveVersion(Song):
    def __init__(self, song_id, title, artist, duration, streams, concert_date, crowd_noise_level):
        super().__init__(song_id, title, artist, duration, streams)
        self._concert_date = str(concert_date)
        self._crowd_noise_level = int(crowd_noise_level)

    def apply_echo(self, echo_intensity: int):
        if echo_intensity < 0:
            raise ValueError("Echo intensity must be non-negative.")
        extension = self._duration * (self._crowd_noise_level / 10) * echo_intensity
        self._duration += extension
        return self._duration


class PlayList:
    def __init__(self, playlist_id, songs, current_index=0):
        self._playlist_id = str(playlist_id)
        self._songs = list(songs)
        self._current_index = int(current_index)

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song_id):
        for i, song in enumerate(self._songs):
            if song._song_id == song_id:
                self._songs.pop(i)
                return
        raise ValueError(f"Song with ID: {song_id} not found in playlist.")

    def next_song(self):
        if self._current_index + 1 < len(self._songs):
            self._current_index += 1
            return self._songs[self._current_index]
        raise IndexError("No next song in the playlist.")

    def total_duration(self):
        return sum(song._duration for song in self._songs)

    def __str__(self):
        return "PlayList:\n" + "\n".join(str(song) for song in self._songs)

    def __add__(self, other):
        if not isinstance(other, PlayList):
            return NotImplemented
        new_id = self._playlist_id + other._playlist_id
        combined_songs = []
        seen = set()
        for song in self._songs + other._songs:
            if song._song_id not in seen:
                seen.add(song._song_id)
                combined_songs.append(song)
        new_index = min(self._current_index, other._current_index)
        return PlayList(new_id, combined_songs, new_index)


class User:
    def __init__(self, user_id, liked_songs=None, history=None):
        self._user_id = str(user_id)
        self._liked_songs = list(liked_songs) if liked_songs else []
        self._history = list(history) if history else []

    def like(self, song):
        if song not in self._liked_songs:
            self._liked_songs.append(song)

    def play(self, song):
        self._history.append(song)
        song.play()

    def recommend(self):
        if not self._liked_songs:
            return None
        return min(self._liked_songs, key=lambda song: song.get_streams())
  
def run_tests():
    print("=== MUSIC STREAMING SERVICE TESTS ===")
    
    print("\n=== Testing Song Class ===")
    song1 = Song("S001", "Blinding Lights", "The Weeknd", 200, 1000000)
    song2 = Song("S002", "Save Your Tears", "The Weeknd", 215, 500000)
    print(song1)
    print(f"Length: {len(song1)} seconds")
    
    song1.play()
    song1.play()
    print(f"Streams after 2 plays: {song1.get_streams()}") 
    
    
    mashup = song1 + song2  
    print(f"Mashup: {mashup}")
    

    print("\n=== Testing Single Class ===")
    single1 = Single("S003", "Stay", "The Kid LAROI", 138, 2000000, "Pop")
    print(single1)  
    single1.set_genre("Pop-Rock")
    print(f"Updated genre: {single1.get_genre()}")
    

    print("\n=== Testing LiveVersion Class ===")
    live1 = LiveVersion("S004", "Bohemian Rhapsody", "Queen", 354, 5000000, "1985-07-13", 8)
    print(live1)
    original_duration = live1._duration
    live1.apply_echo(1.2)
    print(f"Duration after echo: {live1._duration:.1f}s (was {original_duration}s)")
    

    print("\n=== Testing Playlist ===")
    playlist = PlayList("P001", [song1, song2])
    playlist.add_song(single1)
    playlist.add_song(live1)
    print(playlist) 
    print(f"Total duration: {playlist.total_duration():.1f} seconds")
    

    print("\nCurrent song:", playlist._songs[playlist._current_index])
    print("Next song:", playlist.next_song())  
    

    playlist2 = PlayList("P002", [single1])
    merged = playlist + playlist2  
    print(f"\nMerged playlist has {len(merged._songs)} songs")
    
    print("\n=== Testing User ===")
    user = User("U001")
    user.like(song1)
    user.like(song2)
    user.play(song1)
    user.play(song2)
    

    rec = user.recommend()
    print(f"Recommended song: {rec._title} (streams: {rec.get_streams()})")
    

    print("\n=== Testing Edge Cases ===")
    try:
        bad_song = Song("S005", "Bad", "Artist", -100, 0)  
    except Exception as e:
        print(f"Caught invalid duration: {e}")
    
    try:
        playlist.remove_song("invalid_id") 
    except ValueError as e:
        print(f"Caught missing song: {e}")
    
    try:
        live1.apply_echo(-1)
    except ValueError as e:
        print(f"Caught invalid echo: {e}")

if __name__ == "__main__":
    run_tests()
