class TaskManager:

    def __init__(self):
        self.tasks = []
        pass # No code here yet

    def save_task(self, task):
        if task == "":
            raise Exception("No task provided")
        self.tasks.append(task.lower())
        # Parameters:
        #   task: string representing a single task 
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        #   Throws an exeption if task is empty 
        pass # No code here yet

    def format(self): 

        return "\n".join(self.tasks)
        # Parameters: 
        #   None 
        # Returns: 
        #   A string represent tasks 
        # Side-effects 
        #   Nothing
        pass

    def complete_task(self, task):
        if task.lower() not in self.tasks:
            raise Exception("Task does not exist")
        self.tasks.remove(task.lower())
        # Returns:
        #   None 
        # Side-effects:
        #   Remove task from the task list 
        #   Throws an exception if task is not in the list 
        # No code here yet