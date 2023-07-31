from lib.todo_list import *
from lib.todo import *
import pytest 

'''
Given a todo, 
add todo to a todo list property 
'''

def test_add_todo_to_todo_list():
    todo_list = TodoList()
    todo = Todo("Sleep")
    todo_list.add(todo)
    assert todo_list.incomplete() == [todo]


'''
Given a completed todo, 
return a list of completed todos
'''

def test_complete_when_all_the_tasks_are_completed(): 
    todo_list = TodoList()
    todo = Todo("Sleep")
    todo.mark_complete()
    todo_list.add(todo)
    assert todo_list.complete() == [todo]


'''
Given a completed todo and an incomplete todo, 
return a list of completed todos
'''

def test_complete_when_some_tasks_are_completed(): 
    todo_list = TodoList()
    todo = Todo("Sleep")
    todo.mark_complete()
    todo_2 = Todo("Eat")
    todo_list.add(todo)
    todo_list.add(todo_2)
    assert todo_list.complete() == [todo]

'''
Given an incomplete todo, 
return a list of incomplete todos
'''

def test_incomplete_when_all_the_tasks_are_incomplete(): 
    todo_list = TodoList()
    todo = Todo("Sleep")
    todo_list.add(todo)
    assert todo_list.incomplete() == [todo]

'''
Given multiple todos, 
marks all todos complete 
'''

def test_give_up():
    todo_list = TodoList()
    todo_1 = Todo("Sleep")
    todo_list.add(todo_1)
    todo_2 = Todo("Eat")
    todo_list.add(todo_2)
    todo_list.give_up()
    assert todo_list.complete() == [todo_1, todo_2]


'''
Given all the todos are completed, 
raise an error if the user gives up 
'''

def test_give_up_raises_error_if_all_todos_are_completed(): 
    todo_list = TodoList()
    todo = Todo("Sleep")
    todo.mark_complete()
    todo_list.add(todo)
    with pytest.raises(Exception) as e: 
        todo_list.give_up()
    assert str(e.value) == "No todo to give up"