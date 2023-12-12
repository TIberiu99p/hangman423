import json

class Hint:
    def __init__(self, json_file):
        with open(json_file, 'r') as file:
            self.words_hints = json.load(file)

    def get_hint(self, word):
        for difficulty in self.words_hints:
            if word in self.words_hints[difficulty]:
                return self.words_hints[difficulty][word]
        return "No hint available."
