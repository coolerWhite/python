#!/usr/bin/python3
import sys

def cli_echo(name, message):
    print(f"Hi {name}, message to you: {message}")
    
if __name__ == "__main__":
    print("Только cli")

    if "--name" in sys.argv:
        name_index = sys.argv.index("--name") + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]
    
    if "--message" in sys.argv:
        message_index = sys.argv.index("--message") + 1
        if message_index < len(sys.argv):
            message = sys.argv[message_index]

cli_echo(name, message)