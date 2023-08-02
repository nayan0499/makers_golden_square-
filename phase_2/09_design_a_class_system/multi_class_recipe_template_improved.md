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
    
    def __init__(self): 
        pass 
    
    def add(self, diary_entry):
        # diary_entry: an instance of DiaryEntry 
        # diary_entry will be added to the diary_entries property 
        pass

    def get_all_diary_entries(self):
        # return all diary entries 
        pass

class DiaryEntry:
    
    def __init__(self, title, contents): 
        # arguments: 
            # title: str 
            # contents: str 
        # side effects: 
            # set title as title property 
            # set contents as contents property 
        # returns None 
        pass
    
class TaskList:
    
    def __init__(self): 
        pass

    def add(self, task):
        # arguments: 
        #   task: an instance of Task 
        # side effects: 
        #   add task to the list of tasks property 

        pass


class Task:
    
    def __init__(self, task): 
        # arguments:
            # task: str 
        # side effects: 
            # set task property as task 
        pass 


class PhoneNumberExtractor: 
    
    def __init__(self):
        pass 

    def extract(self, content):
        # arguments:
        #   diary: an instance of diary 
        # return phone number as a string 
        pass


class ReadableEntryFinder: 
    
    def __init__(self):
        pass

    def get_diary_entry_based_on_reading_speed_and_time(self, wpm, minutes):
        # returns diary entry that is the most suitable to read in the time given. 



```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

"""
Given a Diary entry
We see that entry reflected in the diary entries list
"""
diary = Diary()
diary_entry_1 = DiaryEntry("Monday 1st August", "I am learning to design a multi-class program")
diary.add_diary_entry(diary_entry_1)
diary.list_diary_entries() # => [diary_entry_1]

"""
Given two diary entries
We see that entry reflected in the diary entries list
"""
diary = Diary()
diary_entry_1 = DiaryEntry("Monday 1st August", "I am learning to design a multi-class program")
diary_entry_2 = DiaryEntry("Monday 2nd August", "I am learning to tdd")
diary.add_diary_entry(diary_entry_1)
diary.add_diary_entry(diary_entry_2)
diary.list_diary_entries() # => [diary_entry_1, diary_entry_2]



'''
Given time and speed
We should get the most suitable diary entry to read 
'''
def test_find_best_entry_for_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("Sunday 1976", "Best day ever")
    diary_entry2 = DiaryEntry("Monday 1977", "My beachball got lost on the beach today!")
    diary_entry3 = DiaryEntry("Friday 1978", "I finished all my homework")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.find_best_entry_for_reading_time(2, 4) == diary_entry2

def test_find_best_entry_for_reading_time_when_entry_words_are_less_than_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("Sunday 1976", "Best day ever")
    diary_entry2 = DiaryEntry("Monday 1977", "My beachball got lost on the beach")
    diary_entry3 = DiaryEntry("Friday 1978", "I finished all my homework")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.find_best_entry_for_reading_time(2, 4) == diary_entry2

def test_find_best_entry_for_reading_time_when_entry_words_are_greater_than_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("Sunday 1976", "Best day ever")
    diary_entry2 = DiaryEntry("Monday 1977", "My beachball got lost on the beach today and")
    diary_entry3 = DiaryEntry("Friday 1978", "I finished all my homework")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.find_best_entry_for_reading_time(2, 4) == diary_entry3


'''
Given a list of todos, 
list the todos 
'''
diary = Diary()
todo_1 = Todo()
diary.add_todo(todo_1)
diary.list_todos() == [todo_1]


'''
Given a diary with 1 entries, 
we should see the phone numbers from 1 entries 
'''
diary = Diary()
diary_entry1 = DiaryEntry("Sunday 1976", "Best day ever........ Phone Number: Nayan - 07450989861")
diary.add(diary_entry1)
diary_entry1.extract_phone_number()
phone_no_1 = Phone_Number("Nayan", "07450989861")
diary.list_phone_numbers == [phone_no_1]

'''
Given a diary with 2 entries with the same phone number and name 
we should only see one phone number saved 
'''
diary = Diary()
diary_entry1 = DiaryEntry("Sunday 1976", "Best day ever........ Phone Number: Nayan - 07450989861")
diary_entry2 = DiaryEntry("Sunday 1999", "The worst day ever........ Phone Number: Nayan - 07450989861")
diary.add(diary_entry1)
diary.add(diary_entry2)
diary_entry2.extract_phone_number()
diary_entry2.extract_phone_number()
phone_no_1 = Phone_Number("Nayan", "07450989861")
phone_no_2 = Phone_Number("Nayan", "07450989861")
diary.list_phone_numbers == [phone_no_1]



```



## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

# Diary.py

"""
Given an empty diary 
We see an empty list of diary entries 
"""

diary = Diary()
diary.list_diary_entries() # []

'''
Given a list of todos, 
list the todos 
'''
diary = Diary()
diary.list_todos() == []

'''
Given a diary, 
we should see an empty list of phone numbers 
'''
diary = Diary()
diary.list_phone_numbers() == []


# DiaryEntry.py

"""
Given a title and contents
We can create a diary entry with it
"""

diary_entry = DiaryEntry("Example title", "Example content")
diary_entry.title  # => "Example title"
diary.entry.content  # => "Example content"


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
