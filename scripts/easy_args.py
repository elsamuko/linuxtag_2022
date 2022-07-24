#!/usr/bin/env python3
# https://typer.tiangolo.com/
# python3 -m pip install typer

import typer


def func(fruit: str, count: int = 4):
    print(f"{count} x {fruit}")


if __name__ == "__main__":
    typer.run(func)
