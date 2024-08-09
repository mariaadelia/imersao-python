#!/usr/bin/env python3

def famous_births(dicitionary):  
    # Converter o dicionário para lista de tuples (key, value)
    items = list(dicitionary.items())

    #item[1] porquê o 0 é a key, o date_of_birth é o nome da key dentro do dicionário
    sorted_items = sorted(items, key=lambda item: item[1]['date_of_birth'])
    # transformando a lista de volta para dicionário
    sorted_items_dictionary = dict(sorted_items)
          
    for key, inside_dic in sorted_items_dictionary.items():
        name = inside_dic['name']
        birth = inside_dic['date_of_birth']
        print(f"{name} is a great scientist born in {birth}.")

 

    


def main():        
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    famous_births(women_scientists)
   




if __name__ == "__main__":
    main()