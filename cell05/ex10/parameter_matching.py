#!/usr/bin/env python3
import sys

def parameter_receiving():    
    parameter = ''.join(sys.argv[1:])    

    if parameter:
        parameter_user = input(f"What was the parameter? ")

        if(parameter == parameter_user):
            print("Good job!")
        else:
            print("Nope, sorry...")
    else:
        print("none")


if __name__ == "__main__":
    parameter_receiving()