
class MusicTracker:

    def __init__(self):
        self.tracks = []

    def add(self, track):
        if track == "":
            raise Exception("No track input")
        if track not in self.tracks:
            self.tracks.append(track)
        

    def track_list(self):
        print(self.tracks)
        return self.tracks


music_tracker = MusicTracker()
(music_tracker.add({"Artist": "Beyonce", "Song":"Halo"}))
(music_tracker.add({"Artist": "Beyonce", "Song":"Single ladies"}))
print(music_tracker.track_list())