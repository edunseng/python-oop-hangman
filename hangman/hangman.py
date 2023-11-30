import random
import time
import re

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    random_word: str
        Word to be guesst in the game picked at random from the list of words.
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    hidden_word: str
        A string of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be '_ _ _ _ _'
        If the player guesses 'a', the list would be 'a _ _ _ _'
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    wrong_guesses: list
        A list of the letters that have already been tried
    correct_guesses: list
         A list of the letters of the word which have been guessed.

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    hide_word()
        Hides the word by replacing the letters with '_' and 
        gradually reveals correct guesses.
    hungman_winner()
        returns 'True' if the hidden_word does not contain any 
        underscore characters.
    hungman_looser()
        returns 'True' when the player has used all of their 
        lives (num_lives == 0).
    hungman_game_over()
        returns 'True' if either hangman_winner() or hangman_looser() 
        is true; otherwise, it returns 'False'. This allows the game 
        flow to loop until this function becomes 'True'.
    print_game_status()
        clears the screen and displays information about the correct 
        and wrong guesses so far, the remaining lives, and the remaining 
        letters to guess. The correct stick figure state index is selected 
        from a list of six states.
    '''
    def __init__(self, random_word):
        # TODO 2: Initialize the attributes as indicated in the docstring
        self.word = random_word
        self.num_lives = len(status)-2 
        self.correct_guesses = list() 
        self.wrong_guesses = list() 
        self.num_letters = len(set(random_word)) 
        # TODO 2: Print two message upon initialization:
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed} refactored as output of hide_word(): str
        self.print_game_status()

    def check_letter(self, letter) -> None:
        '''
        Correct guesses are added to the correct_guesses list, 
        while wrong guesses are added to the wrong_guesses list. 
        The num_lives and num_letters variables are reduced by 1 
        for a miss or a hit, respectively.
        
        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter 
        # -> is processed in hide_word()
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        
        # Check if the guess is in the word.
        hit = self.word.__contains__(letter) and not self.correct_guesses.__contains__(letter)
        if (hit):
            #print(f"Good guess! '{letter}' is in the word.")
            self.correct_guesses.append(letter)
            self.num_letters = self.num_letters - 1
            #time.sleep(1.5)
        else: 
            #print(f"Sorry, '{letter}' is not in the word. You have {self.num_lives-1} lives left.")
            self.wrong_guesses.append(letter)
            self.num_lives = self.num_lives - 1
            #time.sleep(1.5)
        

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        while (self.hangman_game_over() == False):
            self.print_game_status()
            letter = input("\nEnter a single letter:")
            # Check 1: letter is alphabetical and has a length = 1
            letter = re.search('^[a-z]$',letter)
            match letter:                 
                case None: # Letter is an invalid input                                        
                    print ('Please, enter just one character.')
                    time.sleep(1.5)
                case _: # letter is a valid input                   
                    self.letter =  letter.string.lower()
                    letter = self.letter
                    tried_before = self.wrong_guesses.__contains__(letter) or self.correct_guesses.__contains__(letter)                    
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
                    if (tried_before):
                        print(f"{letter} was already tried.")
                        time.sleep(1.5) 
        # TODO 3: If the letter is valid, call the check_letter method                                           
                    else: 
                        self.check_letter(letter)
    
    def hide_word(self):
       # Hides the word by replacing the letters with '_' and 
       # gradually reveals correct guesses.
        self.hidden_word = str()  
        for self.letter in self.word:
            if self.letter in self.correct_guesses:
                self.hidden_word += f"{self.letter} "
            else:
                self.hidden_word += "_ "
        return self.hidden_word
    
    def print_game_status(self,win=False):
        print("\033c", end='') #clear output
        if win == True:
            print(status[-1])
            print (self.hide_word())
        else:
            print(status[len(self.wrong_guesses)])
            print (f"The mistery word has {str(self.num_letters)} characters")
            print (self.hide_word())

    def hangman_winner(self):
        if "_" not in self.hide_word():
            return True
        return False
    
    def hangman_looser(self):
        if self.num_lives == 0:
            return True
        return False
    
    def hangman_game_over(self):
        if self.hangman_looser():
            self.print_game_status()
            print(f"You lost! The word was {self.word}")
            quit()
        if self.hangman_winner():
            self.print_game_status(True)
            print("Congratulations! You won!") 
            quit()
        game_over = self.hangman_winner() or self.hangman_looser()        
        return game_over


def play_game(random_word):
    # As an aid, part of the code is already provided:
    game = Hangman(random_word)
    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    game.ask_letter()
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations! You won!"
    # If the user runs out of lives, print "You lost! The word was {word}"
    game.hangman_game_over() 

if __name__ == '__main__':
    status = ['''
  >>>>>>>>>>>>Hangman<<<<<<<<<<
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
!!!! Final Attempt !!!! 
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
YOU LOST !
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''', '''
* YOU SAVED ME ! *
     
 \O/  
  |  
 / \   
=========''']

    def random_word():
        word_list = ["apple", "banana", "cherry", "mango", "strawberry"]
        return random.choice(word_list)
    play_game(random_word())
