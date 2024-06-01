#!/usr/bin/python3

import click

@click.command()
@click.option("--greeting", default="H", help="How greet")
@click.option("--name", default="T", help="Who")

def greet(greeting, name):
    print(f"{greeting} {name}")

if __name__ == "__main__":
    greet()