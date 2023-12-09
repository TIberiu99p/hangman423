import random

word_list = ['apples', 'bananas', 'pears', 'cherries', 'lemon']
word = random.choice(word_list)

while True:
    guess = input("Enter a single lowercase character: ").lower()
    
    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            print(f"{guess} is in {word}")
            break
        else:
            print(f"{guess} not in the word try again")
    else:
        print("Invalid input. Please enter a single lowercase character.")
