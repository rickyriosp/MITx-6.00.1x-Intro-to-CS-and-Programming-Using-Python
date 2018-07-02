# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:05:21 2018

@author: nas7ybruises
"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = ''
    mistakesMade = 0
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')
    while(mistakesMade < 8):        
        print('You have ' + str(8-mistakesMade) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ')
        letter = letter.lower()
        
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: " \
                  + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed = lettersGuessed + letter
            if letter in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            else:
                print('Oops! That letter is not in my word: ' \
                      + getGuessedWord(secretWord, lettersGuessed))
                mistakesMade += 1
        
        print('-------------')
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
        elif mistakesMade == 8:
            print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
