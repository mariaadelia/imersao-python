#!/usr/bin/env python3

try:
    user_age = int(input("Please tell me your age: "))
    print(f"You are currently {user_age} years old.")

    print(f"In 10 years, you'll be {user_age + 10} years old.")
    print(f"In 20 years, you'll be {user_age + 20} years old.")
    print(f"In 30 years, you'll be {user_age + 30} years old.")

except ValueError:
    print("Not a valid number. Try again.")