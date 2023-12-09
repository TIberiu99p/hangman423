import random
import string

word_list = ['apples', 'bananas', 'pears', 'cherries', 'lemon']
alphabet_list = list(string.ascii_lowercase)
word = random.choice(word_list)

while True:
    guess = input("Enter a single lowercase character: ").lower()
    
    if len(guess) == 1 and guess in alphabet_list:
        print("Good input")
        break
    else:
        print("Invalid input. Please enter a single lowercase character.")

print(f"The chosen word is: {word}")



