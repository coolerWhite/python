#!/usr/bin/python3
import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Echo input text")
    parse.add_argument("message", help="Message echo")
    parse.add_argument("--twice", "-t", help="DO it twice", action="store_true")
    args = parse.parse_args()

    print(args.message)
    if args.twice:
        print(args.message)