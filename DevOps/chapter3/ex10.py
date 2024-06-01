#!/usr/bin/python3

import click

@click.group()
def cli():
    pass

@click.group(help="Ship command")
def ships():
    pass

cli.add_command(ships)

@ships.command(help="Sail a ship")
def sail():
    ship_name = "Your ship"
    print(f"{ship_name} is setting sail")

@ships.command(help="List all")
def list_ships():
    ships = ["JB", "YC", "Penelopa"]
    print(f"Ships: {','.join(ships)}")

@click.command(help="Talk to a sailor")
@click.option("--greeting", default="H", help="How greet")
@click.argument("name")
def greet(greeting, name):
    print(f"{greeting} {name}")

if __name__ == "__main__":
    cli()