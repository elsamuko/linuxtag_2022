import unittest
import linuxtag.functions as functions


class TestFunctions(unittest.TestCase):

    def test_add_five(self):
        self.assertEqual(12, functions.add_five(7))
        # self.assertEqual(13, functions.add_five(7))
