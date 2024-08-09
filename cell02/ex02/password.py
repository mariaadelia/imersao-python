#!/usr/bin/env python3

password = "Python is awesome"
usuario_tentativa = input("Digite seu password: ")

if password == usuario_tentativa:
    print("ACCESS GRANTED.")
else:
    print("ACCESS DENIED.")