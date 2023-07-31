class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        self.todo_list.append(todo)
        
    def incomplete(self):
        return [todo for todo in self.todo_list if todo.complete == False]


    def complete(self):
        return [todo for todo in self.todo_list if todo.complete == True]

    def give_up(self):
        if [todo for todo in self.todo_list if todo.complete == True]  != []:
            raise Exception("No todo to give up")
        for todo in self.todo_list: 
            todo.mark_complete()