import random
from difficulty import Difficulty
from hint import Hint
from drawHang import HangmanDrawing
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.hint = Hint('words.json').get_hint(self.word)
        self.hangman_drawing = HangmanDrawing()

    def check_guess(self, guess):
        if guess in self.word:
            print(f"{guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess and self.word_guessed[index] == '_':
                    self.word_guessed[index] = guess

            print("Word: " + " ".join(self.word_guessed))

        else:
            self.num_lives -= 1
            print(f"{guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            drawing_stage = len(self.hangman_drawing.stages) - self.num_lives - 1
            self.hangman_drawing.draw(drawing_stage, self.word_guessed)

        if guess not in self.list_of_guesses:
            self.list_of_guesses.append(guess)


    def ask_for_input(self):
        
        guess = input("Enter a character or type 'hint' for a hint: ").lower()

        if guess == 'hint':
            return 'hint'  
        elif not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please, enter a single alphabetical character.")
            return None  
        elif guess in self.list_of_guesses:
            print("You already tried that letter.")
            return None 
        else:
            return guess  

    def show_hint(self):
        print("Hint:", self.hint)

def play_game(difficulty_level):
    print(f"Received difficulty level: {difficulty_level}")
    difficulty = Difficulty('words.json')  
    word, num_lives = difficulty.get_word_and_lives(difficulty_level)
    game = Hangman([word], num_lives)

    while game.num_lives > 0:
        user_input = game.ask_for_input()

        if user_input == 'hint':
            game.show_hint()
        elif user_input:
            game.check_guess(user_input)

        # Checking if there are no underscores left in 'self.word_guessed' to declare victory
        if '_' not in game.word_guessed:
            print('Congratulations. You won the game!')
            break
        elif game.num_lives == 0:
            print('You lost!')
            break

    if game.num_lives == 0:
        print(f"The correct word was: {game.word}")