#!/usr/bin/env python3

try:
    print("Enter a number less than 25")
    number = int(input())

    if(number <= 25):
        while number <= 25:            
            print(f"Inside the loop, my variable is {number}")
            number += 1
    else:
        print("Error")
    
# Caso o valor seja diferente de um numero        
except ValueError:  
    print("Oops!  Número inválido. Tente novamente...")
  

