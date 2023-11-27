import random
import re

#Create a list containing the names of your 5 favorite fruits.
word_list = ["apple", "banana", "cherry", "mango", "strawberry"]
#Print out the newly created list to the standard output (screen).
hit = False
while (hit == False):
    word = random.choice(word_list)
    guess = "l"
    #guess = input("enter a single letter:")
    # Create a statement that checks if the input is a single alphabetical letter.
    guess = re.search('^[a-z,A-Z]$',guess)
    hit = word.__contains__(guess.string)
    match guess:
        case None:
            print ('Invalid letter. Please, enter a single alphabetical character.')
        case _:
            if (hit):
                print(f"Good guess! '{guess.string}' is in the word: {word}.")
            else: 
                print(f"Sorry, '{guess.string}' is not in the word: {word}. Try again.")
