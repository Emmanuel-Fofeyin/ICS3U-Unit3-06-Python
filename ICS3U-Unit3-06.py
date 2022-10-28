#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Oct 2022
# This program is a number guessing game
# Using if,then and else statements.

import random


def main():
    # this uses if statements to guess a random number

    # input
    random_number = random.randint(0, 9)  # a number between 1 and 9
    guessed_number_as_string = input("Enter a number between 0 and 9: ")

    # process and output
    try:
        guessed_number_as_number = int(guessed_number_as_string)
        if guessed_number_as_number == random_number:
            print("\nYou guessed correctly!")
        else:
            print("\nYou guessed incorrectly, the number was {}.".format(random_number))
    except ValueError:
        print("\nNot good, {} is not an integer.".format(guessed_number_as_string))
    finally:
        print("Thanks for playing.")
        print("\nDone.")



if __name__ == "__main__":
    main()
