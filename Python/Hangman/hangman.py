"""hangman.py: A program that allows someone to play the classic Hangman game against the computer."""

__author__ = "Rens Groot"
__studentNumber__ = "13122304"


import random
from cs50 import get_int

# global variables
filename = "dictionary.txt"


class Lexicon:

    # initializer
    def __init__(self):
        self.words = []

        # load the dictionary of words
        f = open(filename, "r")
        for i in f:
            self.words.append(i.strip())


    # return a list of all words from the dictionary of the given length
    def get_words(self, length):
        self.word_list = []
        for i in self.words:
            if len(i) == length:
                self.word_list.append(i)
        return self.word_list


    # return a single random word of given length, uses `get_words` above
    def get_word(self, length):
        return random.choice(self.get_words(length))


class Hangman:

    # initialize game by choosing a word and creating an empty pattern
    def __init__(self, length, num_guesses):

        # assertions for length and num_guesses
        assert length > 0 and length < 29 and length != 26
        assert num_guesses > 0 and num_guesses < 27

        # counter for the amount of guessed letters
        self.guess_counter = 0

        # getting the word from the Lexicon class
        randomword = Lexicon()
        self.picked_word = randomword.get_word(length)

        # stores the input
        self.length = length
        self.num_guesses = num_guesses

        # create pattern with _ characters
        self.pattern5 = []
        for i in range(self.length):
            self.pattern5.append("_")

        # initializing list of all the guessed letters
        self.guessed_letters = []


    # update the game for a guess of letter
    def guess(self, letter):

        # assertion to check if user inputs a single letter which is not guessed before
        assert str(letter).isalpha() == True and len(str(letter)) == 1
        assert letter not in self.guessed_letters

        # stores input
        self.letter = letter

        # add letter to list of guessed letters
        self.guessed_letters.append(self.letter)

        # counter to go through the word
        counter = 0

        # initializes correct
        correct = False

        # check if letter is in the word
        for i in self.picked_word:
            if i == self.letter.lower():

                # remove the _ character in the list
                del self.pattern5[counter]

                # insert the letter to the list
                self.pattern5.insert(counter, self.letter.lower())

                correct = True

            # counter to go through the word
            counter = counter + 1

        # if letter is not in the word add a used guess
        if correct == False:
            self.guess_counter += 1

        return correct


    # return a nice version of the pattern
    def pattern(self):

        # makes string of list to create the ____ pattern
        self.nice_pattern = ''.join(self.pattern5)

        return self.nice_pattern


    # produce a string of all letter guessed so far
    def guessed_string(self):

        # makes string of list to show the guessed letters
        self.user_guessed = ''.join(self.guessed_letters)

        return self.user_guessed


    # return True if the game is finished and the player has won, otherwise False
    def won(self):

        # check if there is still one or more underscores in pattern 5
        if not '_' in self.pattern5 and self.num_guesses > self.guess_counter:
            return True

        return False


    # return True if the player has lost
    def lost(self):

        # check if the user is out of guesses and the word is not guessed
        if self.num_guesses == self.guess_counter and '_' in self.pattern5:
            return True

        return False


    # return True if the game is finished
    def finished(self):

        # check if game is won or lost
        if self.won() == True or self.lost() == True:
            return True

        return False