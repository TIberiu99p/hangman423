import random

class Hangman:
    def __init__(self,word_list,num_lives = 5):
        self.word_list = word_list#A list of words
        self.word = random.choice(word_list)#The word to be guessed, picked randomly from the word_list
        self.word_guessed = ['_' for _ in self.word]#A list of the letters of the word, with _ for each letter not yet guessed.
        self.num_letters = len(set(self.word))#The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives#The number of lives the player has at the start of the game. 
        self.list_of_guesses = []#A list of the guesses that have already been tried.Set up to empty initially 

