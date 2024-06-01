#!/usr/bin/python3

import sys

def say_it(greet, targer):
    message = f"{greet} {targer}"
    print(message)

if __name__ == "__main__":
    greet = "Hello"
    targer = "Joe"

    if "--help" in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <NAME> -- greet <GREET> "
        print(help_message)
        sys.exit()
    if "--name" in sys.argv:
        name_index = sys.argv.index("--name") + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]
    if "--greet" in sys.argv:
        greet_index = sys.argv.index("--greet") + 1
        if greet_index < len(sys.argv):
            greet = sys.argv[greet_index]
    
say_it(greet, name)
    