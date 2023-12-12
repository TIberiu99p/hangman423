import json
import random

class Difficulty:
    def __init__(self, json_file):
        with open(json_file, 'r') as file:
            self.words = json.load(file)

    def get_word_and_lives(self, level):
        if level == 'easy':
            lives = 7
        elif level == 'medium':
            lives = 5
        else:  # hard
            lives = 3

        word = random.choice(self.words[level])
        return word, lives
