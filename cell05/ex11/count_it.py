#!/usr/bin/env python3
import sys

def parameters_count():
    parameters = sys.argv[1:]
    if parameters:
        print(f"parameters: {len(parameters)}")
        for p in parameters:
            print(f"{p}: {len(p)}")
    else:
        print("none")


if __name__ == "__main__":
    parameters_count()