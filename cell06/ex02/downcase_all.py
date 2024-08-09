#!/usr/bin/env python3
import sys

def downcase_it():    
    try: 
            return_string = ""
            parameters = sys.argv[1:]       

            if len(parameters):                
                return_string = " \n".join([i.lower() for i in parameters])                
            else:
                return_string = "none"               
            
            return return_string
    
    except ValueError:
        print("One of the parameter is not a number!")


print(downcase_it())