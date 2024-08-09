#!/usr/bin/env python3
import sys

def down_case():
    # Igual a dois pois o length conta com o ./nome_script que é executado
    if(len(sys.argv) == 2):              
        parameter_upcase = ''.join(sys.argv[1]).lower()
        print(parameter_upcase)
    else:
        print("none")

if __name__ == "__main__":
    down_case()