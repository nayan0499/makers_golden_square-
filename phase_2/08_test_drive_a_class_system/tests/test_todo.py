from lib.todo import *

'''
Given a todo with a task, 
set the task property to the task and complete property to False
'''
def test_instantiate_todo_object(): 
    todo = Todo("Sleep")
    assert todo.complete == False 
    assert todo.task == "Sleep"