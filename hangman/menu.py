from milestone_5 import play_game

class Menu:
    def __init__(self):
        self.word_list = ['python', 'hangman', 'programming']

    def display(self):
        print("Rules of Hangman:")
        print("1. Guess a letter of the word.")
        print("2. If the letter is in the word, it will be revealed.")
        print("3. If the letter is not in the word, you lose a life.")
        print("4. You have 5 lives in total.")
        print("5. If you lose all lives, you lose the game.")
        print("6. Guess all letters correctly to win the game.")

    def show_rules(self):
        print("Rules of Hangman:")
        print("1. Guess a letter of the word.")
        print("2. If the letter is in the word, it will be revealed.")
        print("3. If the letter is not in the word, you lose a life.")
        print("4. You have 5 lives in total.")
        print("5. If you lose all lives, you lose the game.")
        print("6. Guess all letters correctly to win the game.")

def main():
    menu = Menu()
    
    while True:
        choice = menu.display()
        if choice == '1':
            play_game(menu.word_list)
        elif choice == '2':
            menu.show_rules()
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
