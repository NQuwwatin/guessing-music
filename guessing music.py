#!/usr/bin/env python

import random

def main ():
    """Start a genre music guessing game."""
    print ("Guess the genre music!")

    genre = [
        "rock",
        "pop",
        "hip hop",
        "jazz",
        "classical",
        "disco",
        "heavy metal",
        ]
    
    x = random.choice(genre)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What music I am thinking of? "))

        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
                  
main()