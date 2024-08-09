#!/usr/bin/env python3

try:
    user_number = float(input("Give me a number: "))

    if user_number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Not a valid number. Try again.")