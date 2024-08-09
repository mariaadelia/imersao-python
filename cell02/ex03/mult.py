#!/usr/bin/env python3

print("Enter the first number:")
first_number = int(input())

print("Enter the second number:")
second_number = int(input())

multiplicacao = first_number * second_number

message = ""

if multiplicacao == 0:
    message = "The result is positive and negative."
elif multiplicacao > 0:
    message = "The result is positive."
else:
    message = "The result is negative."

#Print f permite colocar a variável dentro da string
print(f"{first_number} x {second_number} = {multiplicacao}")
print(f"{message} \n")