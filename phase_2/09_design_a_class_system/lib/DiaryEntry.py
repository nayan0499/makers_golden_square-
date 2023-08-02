from lib.PhoneNumber import *

class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   contents: string
    #   phone_number_list: list of phone numbers

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.phone_numbers = ""

    def extract_phone_number(self):
        if "Phone Number:" in self.contents: 
            name, phone_number = self.contents.split("Phone Number: ")[1].split("-")
            phone_number = PhoneNumber(name.strip(), phone_number.strip())
            self.phone_numbers = phone_number

    def get_phone_numbers(self):
        return self.phone_numbers

    def count_words(self):
        return len(self.contents.split())