#!/usr/bin/env python3
import statistics

def average(parameter):    
    grades_list = []
    # Com o items eu vou acessar os dois itens do dicionário e aí no for eu adiciono em um array as notas
    for name,grades in parameter.items():        
        grades_list.append(grades)

    #Método python para calcular a média
    grades_average = statistics.mean(grades_list)
    
    return grades_average

    


def main():        
    class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
    }
    class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
    }

    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")
   




if __name__ == "__main__":
    main()