#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_noon(self):
        self.assertEqual(max_integer([]), None)

    def test_ress(self):
        self.assertEqual(max_integer([1, 2, 3, 19]), 19)

    def test_maax(self):
        self.assertEqual(max_integer([1, 3, 4, 21]), 21)


if __name__ == '__main__':
    unittest.main()
