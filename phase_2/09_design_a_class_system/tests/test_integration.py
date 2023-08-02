from lib.Diary import *
from lib.DiaryEntry import *
from lib.Task import *
from lib.PhoneNumber import *

def test_get_diary_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Monday 1st August", "I am learning to design a multi-class program")
    diary.add_diary_entry(diary_entry_1)
    assert diary.list_diary_entries() == [diary_entry_1]

def test_get_2_diary_entries(): 
    diary = Diary()
    diary_entry_1 = DiaryEntry("Monday 1st August", "I am learning to design a multi-class program")
    diary_entry_2 = DiaryEntry("Monday 2nd August", "I am learning to tdd")
    diary.add_diary_entry(diary_entry_1)
    diary.add_diary_entry(diary_entry_2)
    diary.list_diary_entries() == [diary_entry_1, diary_entry_2]

def test_find_best_entry_for_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("Sunday 1976", "Best day ever")
    diary_entry2 = DiaryEntry("Monday 1977", "My beachball got lost on the beach today!")
    diary_entry3 = DiaryEntry("Friday 1978", "I finished all my homework")
    diary.add_diary_entry(diary_entry1)
    diary.add_diary_entry(diary_entry2)
    diary.add_diary_entry(diary_entry3)
    assert diary.get_diary_entry_based_on_reading_speed_and_time(2, 4) == diary_entry2

def test_find_best_entry_for_reading_time_when_entry_words_are_less_than_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("Sunday 1976", "Best day ever")
    diary_entry2 = DiaryEntry("Monday 1977", "My beachball got lost on the beach")
    diary_entry3 = DiaryEntry("Friday 1978", "I finished all my homework")
    diary.add_diary_entry(diary_entry1)
    diary.add_diary_entry(diary_entry2)
    diary.add_diary_entry(diary_entry3)
    assert diary.get_diary_entry_based_on_reading_speed_and_time(2, 4) == diary_entry2

def test_find_best_entry_for_reading_time_when_entry_words_are_greater_than_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("Sunday 1976", "Best day ever")
    diary_entry2 = DiaryEntry("Monday 1977", "My beachball got lost on the beach today and")
    diary_entry3 = DiaryEntry("Friday 1978", "I finished all my homework")
    diary.add_diary_entry(diary_entry1)
    diary.add_diary_entry(diary_entry2)
    diary.add_diary_entry(diary_entry3)
    assert diary.get_diary_entry_based_on_reading_speed_and_time(2, 4) == diary_entry3

def test_get_all_todos(): 
    diary = Diary()
    todo_1 = Task("Sleep")
    diary.add_todo(todo_1)
    assert diary.list_todos() == [todo_1]

def test_get_one_phone_number_from_one_diary_entry(): 
    diary = Diary()
    diary_entry1 = DiaryEntry("Sunday 1976", "Best day ever........ Phone Number: Nayan - 07450989861")
    diary_entry1.extract_phone_number()
    diary.add_diary_entry(diary_entry1)
    assert diary.list_phone_numbers()[0].name == "Nayan"
    assert diary.list_phone_numbers()[0].phone_number == "07450989861"