import random

word_list = ['apples', 'bananas', 'pears', 'cherries', 'lemon']
word = random.choice(word_list)


            
def check_guess(guess):  
        if guess.lower() in word:
            print(f"{guess} is in {word}")
            return True
        else:
            print(f"{guess} not in the word try again")
            return False

def ask_for_input():
    while True:
        guess = input("Enter a character")
        if len(guess) == 1 and guess.isalpha():
            if check_guess(guess):
                break
        else:
            print("Wrong input try again")

ask_for_input()