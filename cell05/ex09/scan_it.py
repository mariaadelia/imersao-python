#!/usr/bin/env python3
import re
import sys

def scan_parameter():
    size_argument = sys.argv[1:]
    if len(size_argument) == 2:  
        find_arguments = re.findall(size_argument[0], size_argument[1])   
        # Outra forma: size_argument[1].count(size_argument[0]) => outra forma de saber o tamanho sem usar o findall e só usando o listaQueQueroProcurar.count(ValorReferencia)

        if find_arguments:                      
            print(len(find_arguments))
        else:
            print("none")                
    else:
        print("none")    


if __name__ == "__main__":
    scan_parameter()