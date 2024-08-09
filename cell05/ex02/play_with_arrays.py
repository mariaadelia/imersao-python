#!/usr/bin/env python3

def iterate_array():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]   
    new_array = []

    for number in original_array:
        if number > 5:
            new_array.append(number + 2)

    print(f"Original array: {original_array}")
    print(f"New array: {new_array}")

if __name__ == "__main__":
    iterate_array()