#!/usr/bin/env python3
import sys

def array_of_names(parameter):        
    list_of_strings = []
    # Com o items eu vou acessar os dois itens do dicionário e aí no for eu adiciono em um array
    for name,surname in parameter.items():
        new_name = name.capitalize()
        new_surname = surname.capitalize()
        list_of_strings.append(f"{new_name} {new_surname}")

    return list_of_strings

    


def main():        
    persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
    }

    
    print(array_of_names(persons))




if __name__ == "__main__":
    main()