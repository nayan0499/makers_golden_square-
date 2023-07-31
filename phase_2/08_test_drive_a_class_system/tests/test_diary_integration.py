from lib.diary import *
from lib.diary_entry import *

"""
Given one diary entry 
We should be able to see diary entry instances
"""
def test_add_one_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry("Sunday 1976", "Best day ever")
    diary.add(diary_entry)
    assert diary.all() == [diary_entry]

"""
Given one diary entry 
We should be able to see the number of words in all diary entries 
"""
def test_count_words_in_one_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry("Sunday 1976", "Best day ever")
    diary.add(diary_entry)
    assert diary.count_words() == 3

"""
Given zero diary entries
We should be able to see the number of words in all diary entries 
"""
def test_count_words_with_no_diary_entry():
    diary = Diary()
    assert diary.count_words() == 0


"""
Given three diary entries
We should be able to see the number of words in all diary entries 
"""
def test_count_words_in_three_diary_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("Sunday 1976", "Best day ever1")
    diary_entry2 = DiaryEntry("Sunday 1977", "Best day ever2")
    diary_entry3 = DiaryEntry("Sunday 1978", "Best day ever3")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.count_words() == 9

"""
Given one diary entry with title and contents
return the reading time to read the content  
"""
def test_reading_time_for_one_entry():
    diary = Diary()
    diary_entry = DiaryEntry("Sunday 1976", "Best day ever")
    diary.add(diary_entry)
    assert diary.reading_time(2) == 2


"""

"""
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