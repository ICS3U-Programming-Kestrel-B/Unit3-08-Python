#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 21, 2022
# This program asks for a year
# and tells you if the year is
# a leap year or not

import math


def main():
    # introductory paragraph
    print("This program asks for a year")
    print("and tells you if the year is")
    print("a leap year or not")
    print("")

    # input
    # getting user_year
    user_year = input("Enter a year: ")

    # process
    # checking that user_year is an integer
    try:
        user_year = int(user_year)
    except ValueError:
        print("\n")
        print(("Please enter a valid number. {} is not valid.\n").format(user_year))
    finally:
        print("")

    # output
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                print(("{} is a leap year!").format(user_year))
            else:
                print(("{} is not a leap year.").format(user_year))
        else:
            print(("{} is a leap year!").format(user_year))
    else:
        print(("{} is not a leap year.").format(user_year))


if __name__ == "__main__":
    main()
