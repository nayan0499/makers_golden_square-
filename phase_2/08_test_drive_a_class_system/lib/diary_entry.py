import math 

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)
        

    def reading_chunk(self, wpm, minutes):
        number_of_words = wpm * minutes
        last_index = number_of_words+self.first_index
        result = self.contents.split()[self.first_index:last_index]
        self.first_index = number_of_words
        if last_index >= self.count_words():
            self.first_index = 0
        return " ".join(result)