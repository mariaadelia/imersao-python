#!/usr/bin/env python3

user_input = input("What you gotta say? : ")

# Versão sem o break
# while user_input != "STOP":
#     user_input = input("I got that! Anything else? : ")

#Versão com o break
while True:
    if(user_input == "STOP"):
        break        
    user_input = input("I got that! Anything else? : ")