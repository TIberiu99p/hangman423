import random

class Hangman:
    def __init__(self,word_list,num_lives = 5):
        self.word_list = word_list#A list of words
        self.word = random.choice(word_list)#The word to be guessed, picked randomly from the word_list
        self.word_guessed = ['_' for _ in self.word]#A list of the letters of the word, with _ for each letter not yet guessed.
        self.num_letters = len(set(self.word))#The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives#The number of lives the player has at the start of the game. 
        self.list_of_guesses = []#A list of the guesses that have already been tried.Set up to empty initially 

    def check_guess(self,guess):  
        guess = guess.lower()
        if guess in self.word:
            print(f"{guess} is in {word}")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
        if guess not in self.list_of_guesses:
            self.num_letters -= 1
        else:
            print(f"{self.guess} not in the word try again")
            

    def ask_for_input(self):
        while True:
            guess = input("Enter a character").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please ,enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
