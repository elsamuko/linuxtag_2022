#!/usr/bin/env python3

class ContextManager:
    def __init__(self, arg) -> None:
        self.arg = arg

    def __enter__(self):
        print(f"__enter__ : {self.arg}")
        return self.arg

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f"__exit__ : {self.arg}")


with ContextManager("Hello") as ctx:
    print(ctx)

print()

with ContextManager("Hello") as ctx, ContextManager("Hello2") as ctx2:
    print(ctx)
    print(ctx2)

print()

# https://docs.python.org/3/library/contextlib.html#module-contextlib
from contextlib import contextmanager

@contextmanager
def manager_func(*args, **kwds):
    arg = args[0]
    print(f"__enter__ : {arg}")
    try:
        yield arg
    finally:
        print(f"__exit__ : {arg}")

with manager_func("Hello3") as ctx:
    print(ctx)
