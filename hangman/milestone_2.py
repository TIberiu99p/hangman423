import random
import string

word_list = ['apples','bananas','pears','cherries','lemon']
alphabet_list = list(string.ascii_lowercase)
word = random.choice(word_list)
guess = input("Enter a single character")
if(len(guess) >= 1 and guess in alphabet_list):
    print("Good input")
else:
    raise ValueError("Input must be a single character")
print(word)