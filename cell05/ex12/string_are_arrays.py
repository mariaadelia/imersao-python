#!/usr/bin/env python3
import sys
import re

def string_z():
    const_z = "z"
    parameters = sys.argv[1:]
    if len(parameters) == 1:        
        for p in parameters:
            count_zs = p.count(const_z)                       
            #1 - z sendo só z ou mais de um 'z'
            if (count_zs == len(p)) or (count_zs > 1):
                repeated_const = const_z * count_zs
                print(repeated_const)                
            else:
                print("none")                
    else:
        print("none")

#List comprehension
    # z = [i for i in parameters[0] if i == 'z']
    # print(''.join(z))

    #Explanation about how the superior code works
    # z = []

    # for parameter in parameters:
    #     for i in parameter:
    #         if i == 'z':
    #             z.append(i)
    # print(''.join(z))

if __name__ == "__main__":
    string_z()