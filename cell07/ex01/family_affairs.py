#!/usr/bin/env python3
import sys

def find_the_redheads(parameter):
    # Eu estou pegando o name (name da key), setando que o valor que eu quero é red e passando o dictionary que ele tem que procurar e o list para transformar em lista
    red_hair_list = list(filter(lambda name : parameter[name] == "red", parameter))
    return red_hair_list

    


def main():        
    dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck":"red"
   }
    print(find_the_redheads(dupont_family))
   




if __name__ == "__main__":
    main()