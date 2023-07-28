# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
Assumption - just the song name and artist now 

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python


# tracks [{artist: Beyonce, song: Halo}, {artist: Beyonce, song: Halo}]

class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   No parameters
        # Side effects:
        #   Sets the tracks property of the self object
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: a dictionary represent a track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object
        pass # No code here yet

    def track_list(self):
        # Returns:
        #   A list of tracks that have been added
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a track
#adds it to the track list
"""
music_tracker = MusicTracker()
music_tracker.add({"Artist": "Beyonce", "Song":"Halo"})
music_tracker.track_list() # => [{"Artist": "Beyonce", "Song":"Halo"}]

"""
Given two tracks 
#adds both tracks to the track list
"""
music_tracker = MusicTracker()
music_tracker.add({"Artist": "Beyonce", "Song":"Halo"})
music_tracker.add({"Artist": "Beyonce", "Song":"Single ladies"})
music_tracker.track_list() # => [{"Artist": "Beyonce", "Song":"Halo"},{"Artist": "Beyonce", "Song":"Single ladies"}]

"""
Given an empty string as a track
#raise an error 
"""
music_tracker = MusicTracker()
music_tracker.add("") # => "No track input"

"""
Given track has already been added
raise an error 
"""
music_tracker = MusicTracker()
music_tracker.add({"Artist": "Beyonce", "Song":"Halo"})
music_tracker.add({"Artist": "Beyonce", "Song":"Halo"})
music_tracker.add({"Artist": "Beyonce", "Song":"Single ladies"})
music_tracker.track_list() # => [{"Artist": "Beyonce", "Song":"Halo"},{"Artist": "Beyonce", "Song":"Single ladies"}]


"""
Given track list is empty 
returns empty list
"""

music_tracker = MusicTracker()
music_tracker.track_list() # => []

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
