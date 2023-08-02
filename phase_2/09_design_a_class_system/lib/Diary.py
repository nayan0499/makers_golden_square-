class Diary:
    # User-facing properties:
    #   diary_enteries: list of all diary enteries
    #   todo_list: list of all the todo's
    #   phone_numbers: list of all phone numbers

    def __init__(self):
        self.diary_entries = []
        self.todo_list = []
        self.phone_numbers = []

    def add_diary_entry(self, diary_entry):
        self.diary_entries.append(diary_entry)
        self.phone_numbers.append(diary_entry.get_phone_numbers())

    def add_todo(self, todo):
        self.todo_list.append(todo)

    def list_diary_entries(self):
        return self.diary_entries

    def list_todos(self):
        return self.todo_list

    def list_phone_numbers(self):
        return self.phone_numbers

    def count_words(self):
        total_words = 0
        for entry in self.entries_list:
            total_words += entry.count_words()
        return total_words 

    def get_diary_entry_based_on_reading_speed_and_time(self, wpm, minutes):
        maximum_words = wpm * minutes
        entries_with_words_less_than_maximum_words = []
        for entry in self.diary_entries:
            if entry.count_words() <= maximum_words:
                entries_with_words_less_than_maximum_words.append(entry)
        return sorted(entries_with_words_less_than_maximum_words, key=lambda entry: entry.count_words() , reverse=True)[0]

