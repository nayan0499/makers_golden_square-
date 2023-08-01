# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

# nouns - objects
diary entries
reading speed
time 
tasks 
todo list 
diary 
contacts 
phone numbers

# verbs - describing
read my past diary entries
select diary entries
keep track of my tasks
keep a todo list along with my diary
see a list of all of the mobile phone numbers

```
┌────────────────────────────┐
│ Diary                      │
│                            │
│ - diary entry list         │
│ - todo list                │
│ - phone numbers list       │
│                            │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ DiaryEntry              │
│                         │
│ - title                 │
│ - content               │
│ - phone number          │
│                         │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   diary_enteries: list of all diary enteries
    #   todo_list: list of all the todo's
    #   phone_numbers: list of all phone numbers

    def __init__(self):
        pass # No code here yet

    def add_diary_entry(self, diary_entry):
        # Parameters:
        #   diary entry: an instance of DiaryEntry
        # Side-effects:
        #   Adds the diary_entry to the diary_entries property of the self object
        pass # No code here yet

    def add_todo(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Side-effects:
        #   Adds the todo to the todo_list property of the self object
        pass # No code here yet

    def list_diary_entries(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of the diary_entries object
        pass # No code here yet

    def list_todos(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of the todo_list object
        pass # No code here yet

    def list_phone_numbers(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of the phone_numbers object
        pass # No code here yet

    def get_diary_entry_based_on_reading_speed_and_time(self, wpm, minutes):
        # Parameters:
        #   wpm - words per minute the user can read
        #   minutes - time in minutes the user has to read 
        # Returns:
        #   A diary entry which is most suitable for the user to read in the specified time
        pass # No code here yet


class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   contents: string
    #   phone_number_list: list of phone numbers

    def __init__(self, title, artist):
        # Parameters:
        #   title: string
        #   content: string
        # Side-effects:
        #   Sets the title and contents properties
        pass # No code here yet

    def extract_phone_number(self):
        # saves the phone number in phone_numbers property
        # Returns:
        #   None
        pass # No code here yet

     def get_phone_numbers(self):
        # Returns:
        #   A list of the phone numbers
        pass # No code here yet


class PhoneNumber:
    # User-facing properties:
    #   number: int

    def __init__(self, phone_number):
        # Parameters:
        #   phone number: int
        # Side-effects:
        #   Sets the phone number properties
        pass # No code here yet

    def check_phone_number_is_valid(number):
        # checks if the number is valid
        # return true or false
        pass # No code here yet


class Task:
    # User-facing properties:
    #   task: str

    def __init__(self, task):
        # Parameters:
        #   task: str
        # Side-effects:
        #   Sets the task properties
        pass # No code here yet
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a Diary entry
We see that entry reflected in the diary entries list
"""
diary = Diary()
diary_entry_1 = DiaryEntry("Monday 1st August", "I am learning to design a multi-class program")
diary.add_diary_entry(diary_entry_1)
diary.list_diary_entries() # => [diary_entry_1]





```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
