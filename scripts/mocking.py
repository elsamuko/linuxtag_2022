#!/usr/bin/env python3
# python3 -m unittest scripts.mocking

import unittest
from unittest.mock import patch


def original():
    return "original"


class Test(unittest.TestCase):
    @patch(f"{__name__}.original")
    def test_func(self, mock):
        print(f"patching {__name__}.original")
        mock.return_value = "replacement"
        print(original())
