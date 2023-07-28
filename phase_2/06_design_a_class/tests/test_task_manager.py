from lib.task_manager import *
import pytest 


def test_save_single_task():
    task_manager = TaskManager()
    task_manager.save_task("Do the dishes")
    assert task_manager.format() == "do the dishes"

def test_save_multiple_tasks():
    task_manager = TaskManager()
    task_manager.save_task("Do the dishes")
    task_manager.save_task("Walk the dog")
    assert task_manager.format() == '''do the dishes\nwalk the dog'''


def test_save_empty_task(): 
    task_manager = TaskManager()
    with pytest.raises(Exception) as e:
        task_manager.save_task("")  
    
    assert str(e.value)== "No task provided"


def test_complete_task():
    task_manager = TaskManager()
    task_manager.save_task("Do the dishes")
    task_manager.save_task("Walk the dog")
    task_manager.complete_task("Do the dishes")
    assert task_manager.format() == "walk the dog"

def test_completed_task_in_caps():
    task_manager = TaskManager()
    task_manager.save_task("Do the dishes")
    task_manager.save_task("Walk the dog")
    task_manager.complete_task("DO THE DISHES")
    assert task_manager.format() ==  "walk the dog"

def test_completed_task_not_in_list():
    task_manager = TaskManager()
    task_manager.save_task("Do the dishes")
    task_manager.save_task("Walk the dog")
    with pytest.raises(Exception) as e:
        task_manager.complete_task("Watch TV") 
    assert str(e.value) ==  "Task does not exist"