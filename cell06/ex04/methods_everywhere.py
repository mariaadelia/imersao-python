#!/usr/bin/env python3
import sys

def shrink(parameter):
    slice_parameter = slice(8)
    parameter = parameter[slice_parameter]
    return parameter

def enlarge(parameter):
    const_add ='Z'
    total_caracters = 8   
    # Descobrindo quantos caracteres faltam para chegar a 8 caracteres 
    count_z_size = total_caracters - len(parameter)
    #Somando a quantidade de Z's no parametro
    parameter = parameter + (const_add * count_z_size)      
    return parameter

def main():        
    arguments = sys.argv[1:]    
    if arguments:
        for arg in arguments:
            if len(arg) > 8:
                print(shrink(arg))
            elif len(arg) < 8:
                print(enlarge(arg))
            else:
                print(arg)        
    else:
        print("none")




if __name__ == "__main__":
    main()