#!/usr/bin/env python3

try:
    first_number = int(input("Give me the first number: "))
    second_number = int(input("Give me the second number: "))
    print("Thank you!")

    sum = first_number + second_number
    subtraction =  first_number - second_number
    division =  first_number // second_number #// acaba não deixando o número como float
    multiplication = first_number * second_number

    print(f"{first_number} + {second_number} = {sum}")
    print(f"{first_number} - {second_number} = {subtraction}")
    print(f"{first_number} / {second_number} = {division}")
    print(f"{first_number} * {second_number} = {multiplication}")
    
except ValueError:
    print("Not a valid number. Try again.")