#!/usr/bin/python3

import fire

def greet(greeting="Hiya", name="T"):
    print(f"{greeting} {name}")

if __name__ == "__main__":
    fire.Fire(greet)