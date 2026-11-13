import random

class Song:
    def __init__(self, title: str, artist: str, duration: str) -> None:
        self.title = title
        self.artist = artist
        self._duration = duration

    def __str__(self) -> str:
        return f"Title: {self.title} - Artist: {self.artist} - duration: {self._duration}"
    
    def get_duration(self) -> int:
        return self._duration

class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self.songs = []

    def __str__(self) -> str:
        songs = ""
        for i in self.songs:
            songs += f"\n Playlist: {self.name}, song: {i}"
        return songs

    def add_song(self, song: Song) -> None:
        self.songs.append(song)

    def remove_song(self, song: Song) -> None:
        self.songs.remove(song)

    def get_total_duration(self) -> str:
        minutes = 0
        seconds = 0

        for dur in self.songs:
            counted = dur.get_duration().split(":")
            minutes += int(counted[0])
            seconds += int(counted[1])

        if seconds >= 60:
            minutes += seconds // 60
            seconds = seconds % 60
        
        return f"Duration: {minutes}:{seconds:02d}"

    def shuffle(self) -> None:
        random.shuffle(self.songs)
        
#inputs
mine = Playlist("my_playlist")
elite = Song("Elite", "Deftones", "4:01")
hy = Song("hy", "hy", "3:01")
mine.add_song(elite)
mine.add_song(hy)

print(elite)
print(mine)

print(mine.get_total_duration())













