#!/usr/bin/env python3
import sys

def parameter_user():    
    if(len(sys.argv) > 1):
        first_parameter = sys.argv[1]
        print(first_parameter)
    else:
        print("none")



if __name__ == "__main__":
    parameter_user()