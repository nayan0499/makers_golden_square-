from lib.todo_list import *

'''
Given an empty todo list 
I should get an empty list 
'''

def test_incomplete(): 
    todo_list = TodoList()
    assert todo_list.incomplete() == []