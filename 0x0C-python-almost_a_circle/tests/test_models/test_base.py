#!/usr/bin/python3
"""making unittests"""

from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """defination of the base"""

    def test_initialization(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_newid(self):
        b4 = Base(12)
        b5 = Base(15)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 15)

