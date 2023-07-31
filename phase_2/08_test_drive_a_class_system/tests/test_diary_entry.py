from lib.diary_entry import *

"""
Given a title and contents
store the title and contents
"""

def test_add_a_title_and_contents():
    diary_entry = DiaryEntry("Example Tilte", "Example Contents")
    assert diary_entry.title == "Example Tilte" 
    assert diary_entry.contents == "Example Contents"



"""
Given a diary entry
count the number of words in contents
"""

def test_count_words_in_the_contents_of_diary_entry():
    diary_entry = DiaryEntry("Example Tilte", "Example Contents")
    assert diary_entry.count_words() == 2