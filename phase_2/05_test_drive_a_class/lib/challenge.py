class GrammarStats:
    def __init__(self):
        self.check_counter = 0
        self.checks_passed = 0
  
    def check(self, text):
        if text == "":
            raise Exception("No text input provided")
        punctuation_list = [".", "?", "!"]
        last_letter = text[-1]
        self.check_counter += 1
        if last_letter in punctuation_list and text[0].isupper():
            self.checks_passed += 1
            return True
        return False
  
    def percentage_good(self):
        return round((self.checks_passed/self.check_counter)*100)