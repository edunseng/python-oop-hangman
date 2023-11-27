import random
import re

#Create a list containing the names of your 5 favorite fruits.
word_list = ["apple", "banana", "cherry", "mango", "strawberry"]
#Print out the newly created list to the standard output (screen).
print(word_list)

word = random.choice(word_list)
guess = "t"
#guess = input("enter a single letter:")
# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
guess = re.search('^\w$',guess)
match guess:
    case None:
        print ('Oops! That is not a valid input.')
    case _:
        print(f"Good guess!")