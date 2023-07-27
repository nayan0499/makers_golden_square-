from lib.Diary_entry_Ex import *

"""
test the format

test function name - test_format():
assert - "My best day ever: I had a bum surgery"

test the count words 

test function name - test_count_words():
"My best day ever: I had a bum surgery"
assert - int: the number of words in this text: "My best day ever: I had a bum surgery"

test reading_time
test function name - test_reading_time
assert - round(x/200)

test reading_chunk
assert - "words" * 30
0.5m 
60wpm
"""

def test_format():
    diary_entry = DiaryEntry("Title", "content")
    assert diary_entry.format() == "Title: content"
    
def test_count_words():
    diary_entry = DiaryEntry("My best day ever ", "I had a bum surgery ")
    assert diary_entry.count_words() == 9

def test_reading_time():
    diary_entry = DiaryEntry("My best day ever ", "I had a bum surgery "*100)
    assert diary_entry.reading_time(200) == 3
    
def test_reading_chunk():
    diary_entry = DiaryEntry("My best day ever", "I had a bum surgery ")
    string_chunk = "My best day ever: I had a bum"
    assert diary_entry.reading_chunk(2, 4) == string_chunk
    
    
def test_reading_chunk_twice():
    diary_entry = DiaryEntry("My best day ever", "I had a bum surgery ")
    reading_chunk_1 = diary_entry.reading_chunk(1, 2)
    reading_chunk_2 = diary_entry.reading_chunk(1, 2)
    assert reading_chunk_2 == "day ever:"

def test_reading_chunk_twice_with_greater_number_of_words_than_text():
    diary_entry = DiaryEntry("My best day ever", "I had a bum surgery ")
    reading_chunk_1 = diary_entry.reading_chunk(2, 4)
    reading_chunk_2 = diary_entry.reading_chunk(2, 4)
    assert reading_chunk_2 == "surgery"

def test_reading_chunk_thrice():
    diary_entry = DiaryEntry("My best day ever", "I had a bum surgery ")
    reading_chunk_1 = diary_entry.reading_chunk(2, 4)
    reading_chunk_2 = diary_entry.reading_chunk(2, 4)
    reading_chunk_3 = diary_entry.reading_chunk(2, 4)
    assert reading_chunk_3 == "My best day ever: I had a bum"
    