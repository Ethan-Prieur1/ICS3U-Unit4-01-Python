#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that checks if a certain year is a leap year


def main():
    # This function is the main function

    counter = 0
    number_sum = 0

    # Input

    number_as_string = input("Enter a Number: ")

    # Process & Output

    try:
        number_as_int = int(number_as_string)
        while counter <= number_as_int:
            number_sum = number_sum + counter
            counter = counter + 1
        print("The sum is {0}".format(number_sum))
    except Exception:
        print("That Isn't an Integer!")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()
