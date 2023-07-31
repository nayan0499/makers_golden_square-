from lib.diary import *

"""
given no diary entries 
show an empty list 
"""
def test_no_diary_entry():
    diary = Diary()
    assert diary.all() == []    