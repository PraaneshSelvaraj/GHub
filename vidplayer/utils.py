import os
import re
class Utils:
    def __init__(self):
        self.songs_list = None

    def get_songs_list(self, path):
        if self.songs_list: return self.songs_list
        else:
            if not os.path.exists(path): return None

            self.songs_list = []
            for root, _, files in os.walk(path):
                if files:
                    for file_name in files:
                        path = os.path.join(root.replace("D:\\Songs\\", "http://localhost:8000/"), file_name)
                        self.songs_list.append(path)

            return self.songs_list
    
    def get_songs_path(self):
        return "D:\\Songs\\"

    def play_song_path(self, song):
        songs_path = self.get_songs_path()
        songs_list = self.get_songs_list(songs_path)
        pattern = re.compile(re.escape(song), re.IGNORECASE)
        
        for song_path in songs_list:

            if re.search(pattern, song_path):

                return song_path
            
        return None