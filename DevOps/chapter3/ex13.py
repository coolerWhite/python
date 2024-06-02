#!/usr/bin/python3

import click

@click.command()
@click.option('--name', default="Zero", help="Name file")

def none_p(name):
    if name.startswith("p") or name.startswith("P"):
       pass
    else:
       print(f"{name} without has P")
        
if __name__ == "__main__":
    none_p()