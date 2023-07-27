import math 

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.first_index = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        split_title = self.title.split()
        split_contents = self.contents.split()
        return len(split_title) + len(split_contents)
            

    def reading_time(self, wpm):
        number_of_words = self.count_words()
        return round(number_of_words/wpm)

    def reading_chunk(self, wpm, minutes):
        number_of_words = wpm * minutes
        last_index = number_of_words+self.first_index
        result = self.format().split()[self.first_index:last_index]
        self.first_index = number_of_words
        if last_index >= len(self.format().split()):
            self.first_index = 0
        return " ".join(result)
    
