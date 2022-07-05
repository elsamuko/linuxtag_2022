#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("filename")
    parser.add_argument("-v", "--verbose", action="store_true", default=False)
    parser.add_argument("--append", action="append", default=[])

    args = parser.parse_args()

    print(args.filename)
    print(args.append)

    if args.verbose:
        print("verbose is on!")


if __name__ == "__main__":
    main()
