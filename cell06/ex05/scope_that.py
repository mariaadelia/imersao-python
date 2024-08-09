#!/usr/bin/env python3
import sys

def add_one(parameter):
    parameter +=1
    return parameter


def main():        
    number_var = 4
    print(f"Value at the initialization: {number_var}")
    #Duas versões
        # Versão 1
    # number_var = add_one(number_var)
        # Versão 2
    add_one(number_var)
    print(f"Value after the method add_one: {number_var}")



if __name__ == "__main__":
    main()