#!/usr/bin/python3

import argparse

def sail():
    ship_name = "Ship name"
    print(f"{ship_name} is setting sail")

def list_ship():
    ships = ["JB", "YC", "Penelopa"]
    print(f"Ships: {','.join(ships)}")

def greet(greeting, name):
    message = f"{greeting} {name}"
    print(message)

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description='Time control')
    
    parse.add_argument('--twice', '-t', help="Do it TWICE", action='store_true')
    subparse = parse.add_subparsers(dest='func')
    ship_parse = subparse.add_parser('ships', help="Ship commands")
    ship_parse.add_argument('command', choices=['list', 'sail'])

    sailor_parse = subparse.add_parser('sailors', help="Talk to a sailor")
    sailor_parse.add_argument('name',help="Sailors name")
    sailor_parse.add_argument("--greeting", "-g", help="Greeting", default="Ahoy there")

    args = parse.parse_args()
    if args.func == 'sailor':
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ship()
    else:
        sail()