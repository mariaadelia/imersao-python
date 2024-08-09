#!/usr/bin/env python3
import sys

def upper_case():
    if(len(sys.argv) == 2):              
        parameter_upcase = ''.join(sys.argv[1]).upper()
        print(parameter_upcase)
    else:
        print("none")

if __name__ == "__main__":
    upper_case()