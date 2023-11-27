import random
import re

#Create a list containing the names of your 5 favorite fruits.
word_list = ["apple", "banana", "cherry", "mango", "strawberry"]

def check_guess(guess, word):  
    # Convert the guess into lower case.
    guess =  guess.lower()
    guess = re.search('^[a-z]$',guess)
    # Check if the guess is in the word.
    hit = word.__contains__(guess.string)
    match guess: 
        case None:
            print ('Invalid letter. Please, enter a single alphabetical character.')
        case _:
            if (hit):
                print(f"Good guess! '{guess.string}' is in the word: {word}.")
            else: 
                print(f"Sorry, '{guess.string}' is not in the word: {word}. Try again.")
    return hit

def ask_for_input(wordlist=word_list):
    # Iteratively check if the input is a valid guess.
    hit = False
    while (hit == False):
        word = random.choice(wordlist)
        guess = input("Enter a single letter:")
        hit = check_guess(guess, word)

ask_for_input()