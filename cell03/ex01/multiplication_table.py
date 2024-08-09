#!/usr/bin/env python3

print("Enter a number")
number = int(input())
count_table = 0

while count_table < 10:
    multiplication_result = number * count_table
    print(f"{count_table} x {number} = {multiplication_result}")
    count_table += 1