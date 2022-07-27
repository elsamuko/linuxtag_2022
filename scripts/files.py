#!/usr/bin/env python3


def write_sth():
    with open("test.txt", "w") as file:
        file.write("hase")

def read_sth() -> str:
    with open("test.txt", "r") as file:
        return file.read()


write_sth()
print(read_sth())

