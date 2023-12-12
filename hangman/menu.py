from milestone_5 import play_game

class Menu:
    def __init__(self):
        self.word_list = ['python', 'hangman', 'programming']

    def display(self):
        print("Welcome to Hangman!")
        print("1. Start Game")
        print("2. Show Rules")
        print("3. Exit")
        return input("Enter your choice (1-3): ")

    def show_rules(self):
        print("Rules of Hangman:")
        print("1. Guess a letter of the word.")
        print("2. If the letter is in the word, it will be revealed.")
        print("3. If the letter is not in the word, you lose a life.")
        print("4. You have 5 lives in total.")
        print("5. If you lose all lives, you lose the game.")
        print("6. Guess all letters correctly to win the game.")

    def choose_difficulty(self):
        print("Choose difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            print("Chosen difficulty: easy")
            print("You can only make 7 mistakes")
            return 'easy'
        elif choice == '2':
            print("Chosen difficulty: medium")
            print("You can only make 5 mistakes")
            return 'medium'
        elif choice == '3':
            print("Chosen difficulty: hard")
            print("You can only make 3 mistakes")
            return 'hard'
        else:
            print("Invalid choice. Defaulting to Easy.")
            return 'easy'

def main():
    menu = Menu()
    
    while True:
        choice = menu.display()
        if choice == '1':
            difficulty_level = menu.choose_difficulty()
            play_game(difficulty_level)
        elif choice == '2':
            menu.show_rules()
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
