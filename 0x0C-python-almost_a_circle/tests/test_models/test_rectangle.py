#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRec(unittest.TestCase):
    """defination foe rec testing"""

    def test_initialization(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_height_validation(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_width_validation(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-10, 2)
            
