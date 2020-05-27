"""bleep.py: Program that censors messages that contain words that appear on a list of supplied banned words."""

__author__ = "Rens Groot"
__studentNumber__ = "13122304"

from cs50 import get_string
from sys import argv


def main():

    # create a set to store banned words in
    banned_words = set()

    # makes sure the user provides 2 command-line arguments
    if len(argv) != 2:
        print("Usage python bleep.py filename.txt")
        exit(1)

    # open the file and add the words to the banned_words set
    else:
        filename = argv[1]
        with open(filename, "r") as f:
            for i in f:
                banned_words.add(i.strip())

    # prompts the user for a sentence
    sentence = get_string("Enter a sentence: ")

    # splits the string into a list where each word is a list item
    words = sentence.split()

    # create an output string
    output = ""

    # if the word is in the banned_words set, the word is replaced by * characters
    for i in words:
        if i.lower() in banned_words:
            output += len(i) * "*" + " "
        else:
            output += i + " "

    print(output)


if __name__ == "__main__":
    main()

