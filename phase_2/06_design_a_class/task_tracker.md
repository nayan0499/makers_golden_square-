# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them. 

format list of tasks 

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TaskManager:

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Sets the tasks property to self object 
        pass # No code here yet

    def save_task(self, task):
        # Parameters:
        #   task: string representing a single task 
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        #   Throws an exeption if task is empty 
        pass # No code here yet

    def format(self): 
        # Parameters: 
        #   None 
        # Returns: 
        #   A string represent tasks 
        # Side-effects 
        #   Nothing

    def complete_task(self, task):
        # Returns:
        #   None 
        # Side-effects:
        #   Remove task from the task list 
        #   Throws an exception if task is not in the list 
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task, 
save the task and print a list of tasks 
"""
task_manager = TaskManager()
first_task = task_manager.save_task("Do the dishes")
task_manager.format() # => "Do the dishes"

"""
Given two tasks, 
save the tasks and print a list of the tasks 
"""
task_manager = TaskManager()
task_manager.save_task("Do the dishes")
task_manager.save_task("Walk the dog")
task_manager.format() # => "Do the dishes
                      #     Walk the dog"
        

"""
Given an empty task
raise an error 
"""
task_manager = TaskManager()
task_manager.save_task("")# => "No task provided"


"""
Given a completed task, 
remove the task from the list 
"""
task_manager = TaskManager()
task_manager.save_task("Do the dishes")
task_manager.save_task("Walk the dog")
task_manager.complete_task("Do the dishes")
task_manager.format() # => "Walk the dog"


"""
Given a completed task thats not in the list, 
raise an error 
"""
task_manager = TaskManager()
task_manager.save_task("Do the dishes")
task_manager.save_task("Walk the dog")
task_manager.complete_task("Watch TV") # => "Task does not exist"


"""
Given a task in caps, 
remove the task from the list 
"""
task_manager = TaskManager()
task_manager.save_task("Do the dishes")
task_manager.save_task("Walk the dog")
task_manager.complete_task("DO THE DISHES")
task_manager.format() # => "Walk the dog"





```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
