#!/usr/bin/env python3
import sys

def add_ism():
    const_final = "ism"
    parameters = sys.argv[1:]
   
    if len(parameters) > 0:        
        for p in parameters:
            if not p.endswith(const_final):
                print(f"{p}{const_final}")            
    else:
        print("none")


if __name__ == "__main__":
    add_ism()