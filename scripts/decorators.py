#!/usr/bin/env python3


def a_decorator(func):
    def inner(*args, **kwargs):
        print(f"before {func.__name__}")
        rv = func(*args, **kwargs)
        print(f"after {func.__name__}")
        return rv
    return inner


@a_decorator
def func(a,b):
    print("within")
    return a+b

@a_decorator
def func2(a,b):
    print("within 2")
    return a,b


print(func(1,2))
print("")

print(func2(1,2)    )
print("")
