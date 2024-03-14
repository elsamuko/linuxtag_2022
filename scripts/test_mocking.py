#!/usr/bin/env python3
# python3 -m unittest scripts.mocking

import unittest
from unittest.mock import patch, MagicMock, Mock


def original():
    return "original"


def func(arg):
    print(arg.sth())
    try:
        parsed = int(arg)
        print(f"Parsed {arg} to {parsed}")
    except:
        print(f"Could not parse {arg} to int")


class Test(unittest.TestCase):
    @patch(f"{__name__}.original")
    def test_original(self, mock):
        print(f"patching {__name__}.original")
        mock.return_value = "replacement"
        print(original())

    def test_func(self):
        print(f"Mocking arg")
        func(MagicMock())
        print()
        func(Mock())
        print()
