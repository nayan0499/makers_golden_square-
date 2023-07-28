from lib.music_tracker import *
import pytest

def test_add_single_track():
    music_tracker = MusicTracker()
    music_tracker.add({"Artist": "Beyonce", "Song":"Halo"})
    assert music_tracker.track_list() == [{"Artist": "Beyonce", "Song":"Halo"}]

def test_add_multiple_tracks():
    music_tracker = MusicTracker()
    music_tracker.add({"Artist": "Beyonce", "Song":"Halo"})
    music_tracker.add({"Artist": "Beyonce", "Song":"Single ladies"})
    assert music_tracker.track_list() == [{"Artist": "Beyonce", "Song":"Halo"},{"Artist": "Beyonce", "Song":"Single ladies"}]
    
def test_adding_the_same_track_twice():
    music_tracker = MusicTracker()
    music_tracker.add({"Artist": "Beyonce", "Song":"Halo"})
    music_tracker.add({"Artist": "Beyonce", "Song":"Halo"})
    music_tracker.add({"Artist": "Beyonce", "Song":"Single ladies"})
    assert music_tracker.track_list() == [{"Artist": "Beyonce", "Song":"Halo"},{"Artist": "Beyonce", "Song":"Single ladies"}]
    
def test_adding_empty_track():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add("")
    error_message = str(e.value)
    assert error_message == "No track input"  

def test_getting_empty_track_list():
    music_tracker = MusicTracker()
    assert music_tracker.track_list() == []