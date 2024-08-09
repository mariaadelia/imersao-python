#!/usr/bin/env python3

try:
    number = int(input("Your number: "))
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
# Caso o valor seja diferente de um numero        
except ValueError:  
    print("Oops!  Número inválido. Tente novamente...")
  

