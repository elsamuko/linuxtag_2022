#!/usr/bin/env python3
# comments
"""
    multiline
    comments
"""


class Hase:
    name = "Hase"  # global static
    __height = 10  # 'private' static members start with __

    def __init__(self, ears, legs) -> None:
        """ constructor """
        self.ears = ears   # public members
        self.__legs = legs  # 'private' members start with __

    def __repr__(self) -> str:
        return f"I'm {Hase.name} with {self.ears} ears and {self.__legs} legs"

    @property
    def legs(self):
        """ getter """
        return self.__legs

    @legs.setter
    def legs(self, legs):
        """ setter """
        self.__legs = legs


# run only if file is called directly
if __name__ == "__main__":
    hase = Hase(4, 5)
    hase.legs = 6

    print(hase)
