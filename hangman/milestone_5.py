import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess in self.word:
            print(f"{guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess and self.word_guessed[index] == '_':
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"{guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

        if guess not in self.list_of_guesses:
            self.list_of_guesses.append(guess)

    def ask_for_input(self):
        guess = input("Enter a character: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter.")
        else:
            self.check_guess(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

# Example usage
word_list = ['python', 'hangman', 'programming']
play_game(word_list)