#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : March 2025
# This program tells the user if the inputted integer is positive or negative


def main():
    # creates a variable and asks the user to assign a value
    user_number = int(input("choose a number greater or lesser than 0: "))

    # checks if the inputted number is more than 0
    if user_number < 0:
        print("your number is a negative integer")

    # checks if the inputted number is less than 0
    elif user_number > 0:
        print("Your number is a positive integer")

    # if the number is not less or more than 0 then it must be 0
    else:
        print("your number is 0")


if __name__ == "__main__":
    main()
