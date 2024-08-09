#!/usr/bin/env python3

try:
    number = int(input("Your number: "))

    if number == 0:
        print("This number is both positive and negative.")
    elif number < 0:
        print("This number is negative.")
    #Caso seja maior e diferente de 0
    else:
        print("This number is positive.")
# Caso o valor seja diferente de um numero        
except ValueError:  
    print("Oops!  Número inválido. Tente novamente...")
  
