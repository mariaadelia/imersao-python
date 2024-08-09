#!/usr/bin/env python3

import sys

def numbers_range():    
    try: 
        parameters = sys.argv[1:]       

        if len(parameters) == 2:
            parameter_one = int(parameters[0])
            parameter_two = int(parameters[1]) 
            array_range = [i for i in range(parameter_one, parameter_two + 1)]            
            print(array_range)
        else:
            print("none")   

    except ValueError:
        print("One of the parameter is not a number!")
    

if __name__ == "__main__":
   numbers_range()