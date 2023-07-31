class Diary:
    def __init__(self):
        self.entries_list = []

    def add(self, entry):
        self.entries_list.append(entry)

    def all(self):
        return self.entries_list

    def count_words(self):
        total_words = 0
        for entry in self.entries_list:
            total_words += entry.count_words()
        return total_words 


    def reading_time(self, wpm):
        total_reading_time = 0
        for entry in self.entries_list:
            total_reading_time += entry.reading_time(wpm)
        return total_reading_time

    def find_best_entry_for_reading_time(self, wpm, minutes):
        maximum_words = wpm * minutes
        entries_with_words_less_than_maximum_words = []
        for entry in self.entries_list:
            if entry.count_words() <= maximum_words:
                entries_with_words_less_than_maximum_words.append(entry)
        return sorted(entries_with_words_less_than_maximum_words, key=lambda entry: entry.count_words() , reverse=True)[0]
                
