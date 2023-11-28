import random
import re

'''
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

def ask_for_input(fruits=word_list):
    # Iteratively check if the input is a valid guess.
    hit = False
    while (hit == False):
        word = random.choice(fruits)
        guess = input("Enter a single letter:")
        hit = check_guess(guess, word)
'''
#Create a class called Hangman.
class Hangman:  
    # __init__ is the constructor, and .__init__() sets the initial state of the object.
    # Inside the class, create an __init__ method to initialise the attributes of the class.
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives # The number of lives the player has at the start of the game.
        self.word_guessed = list() # A list of the letters of the word, with _ for each letter not yet guessed.
        self.list_of_guesses = list() # A list of the guesses that have already been tried.
        self.num_letters = int()  # The number of UNIQUE letters in the word that have not been guessed yet.
        # self.word = word #The word to be guessed, picked randomly from the word_list.
        # self.guess = guess # User input

    def check_guess(self, guess, word):
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
      
    # Iteratively check if the input is a valid guess.
    def ask_for_input(self):
        hit = False
        while (hit == False):
            word = random.choice(self.word_list)
            guess = input("Enter a single letter:")
            hit = self.check_guess(guess, word)

word_list = ["apple", "banana", "cherry", "mango", "strawberry"]
game = Hangman(word_list,5)
game.ask_for_input()
# Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.