import random
import re
import time
status = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

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
    def __init__(self, random_word):
        self.word = random_word
        #self.hidden_word = str()  
        self.num_lives = len(status)-1 # The number of lives the player has at the start of the game, depends on status elements.
        self.correct_guesses = list() # A list of the letters of the word, with _ for each letter not yet guessed.
        self.wrong_guesses = list() # A list of the guesses that have already been tried.
        self.num_letters = len(set(random_word)) # The number of UNIQUE letters in the word that have not been guessed yet.                

   
    # Iteratively check if the input is a valid guess.
    def ask_for_input(self):
        hit = False
        while (hit == False) or not (self.hangman_game_over()):
            self.print_game_status()
            if self.hangman_looser():
                print("\nSorry, but you have lost.")
                print ("The word was " + self.word)
                print ("\nGoodbye!\n")
                quit()
            guess = input("\nEnter a single letter:")
            hit = self.check_guess(guess)

    def check_guess(self, letter):
        # Convert the guess into lower case.
        letter = re.search('^[a-z]$',letter)
        # Check if the guess is in the word.
        match letter: 
            case None:
                print ('Invalid letter. Please, enter a single alphabetical character.')
                time.sleep(4.5)
                return False
            case _:
                self.letter =  letter.string.lower()
                letter = self.letter
                hit = self.word.__contains__(letter) and not self.correct_guesses.__contains__(letter)
                tried_before = self.wrong_guesses.__contains__(letter) or self.correct_guesses.__contains__(letter)
                if (hit):
                    print(f"Good guess! '{letter}' is in the word.")
                    self.correct_guesses.append(letter)
                    self.num_letters = self.num_letters - 1
                    time.sleep(1.5)
                elif (tried_before):
                    print(f"You've tried '{letter}' before! Try another guess.")
                    time.sleep(1.5)
                else: 
                    print(f"Sorry, '{letter}' is not in the word. You have {self.num_lives-1} lives left.")
                    self.wrong_guesses.append(letter)
                    self.num_lives = self.num_lives - 1
                    time.sleep(1.5)
        return hit 
    
    def hide_word(self):
        self.hidden_word = str()  
        for self.letter in self.word:
            if self.letter in self.correct_guesses:
                self.hidden_word += f"{self.letter} "
            else:
                self.hidden_word += "_ "
        return self.hidden_word
    
    def hangman_winner(self):
        if "_" not in self.hide_word():
            return True
        return False
    
    def hangman_looser(self):
        if self.num_lives == 0:
            return True
        return False
    
    def hangman_game_over(self):
        return self.hangman_winner() or self.hangman_looser()
                        
    def print_game_status(self):
        print("\033c", end='') #clear output
        print(status[len(self.wrong_guesses)])
        print ('Word: ' + self.hide_word())
        print ("Letters to guess: "+str(self.num_letters))
        print ('Lives: '+ str((self.num_lives )))
        print()
        print ('Missed Letters: ',end=" ")
        for self.letter in self.wrong_guesses:
            print (self.letter, end=" ")
        print()
        print('Hits: ', end=" ")
        for self.letter in self.correct_guesses:
            print (self.letter, end=" ")

def random_word():
    word_list = ["apple", "banana", "cherry", "mango", "strawberry"]
    return random.choice(word_list)
    
def main():       
    game = Hangman(random_word())
    game.ask_for_input()
    if game.hangman_winner():
        print("\n Congratulations! You have won!!") 
        print ("The word was " + game.word)
        print ("\nGoodbye!\n")
        quit()

if __name__ == "__main__":
    main()    