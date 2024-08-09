#!/usr/bin/env python3

def greetings(name = 'noble stranger'):
    message = ''

    if isinstance(name,str):
        message = f"Hello, {name}."        
    else:
        message = "Error! It was not a name."

    return print(message)


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)