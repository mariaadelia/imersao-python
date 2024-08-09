#!/usr/bin/env python3
import sys

def count_parameter():        
    lenght_argument = len(sys.argv) - 1
    print(f"Number of parameters: {lenght_argument}")    


if __name__ == "__main__":
    count_parameter()