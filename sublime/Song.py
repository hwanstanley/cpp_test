class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        songs = set()
        next_one = self
        while next_one:
            if next_one.name in songs:
                return True
            else:
                songs.add(next_one.name)
                next_one = next_one.next or None
        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second);
second.next_song(first);
    
print(first.is_repeating_playlist())