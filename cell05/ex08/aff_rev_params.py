#!/usr/bin/env python3
import sys

def reverse_order():
    size_argument = sys.argv[1:]
    if len(size_argument) > 2:                       
        size_argument.reverse()
        reversed_order = "\n".join(size_argument) 
        
        print(reversed_order)
        
    else:
        print("none")    


if __name__ == "__main__":
    reverse_order()