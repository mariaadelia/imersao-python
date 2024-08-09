#!/usr/bin/env python3

def iterate_array():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]   
    new_array = []

    for number in original_array:
        if number > 5:
            new_array.append(number + 2)

    lista_sem_duplicadas = set(new_array)

    print(f"{original_array}")
    print(f"{lista_sem_duplicadas}")


if __name__ == "__main__":
    iterate_array()