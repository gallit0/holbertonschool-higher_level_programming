#!/usr/bin/python3
"""Module"""


import unittest
from models.rectangle import Rectangle


class testsNumber0(unittest.TestCase):
    """Test of Base() for assigning
    automatically an ID exists"""
    def test_0(self):
        self.r1 = Rectangle(1, 2)
        self.assertEqual(self.r1.id, 19)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)
        self.r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r2.id, 5)
    def test_1(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        
class TestsNumber1(unittest.TestCase):
    def test_0(self):
        self.r3 = Rectangle(3, 3)
        self.r4 = Rectangle(1, 2)
        self.assertEqual(self.r3.area(), 9)
        self.assertEqual(self.r3.__str__(), '[Rectangle] (17) 0/0 - 3/3')
        self.assertEqual(self.r4.to_dictionary(), {'id': 18, 'width': 1, 'height': 2, 'x': 0, 'y': 0})

class TestDisplay(unittest.TestCase):
    def setUp(self):
        rd2 = Rectangle(1, 1, 1, 0)
        rd3 = Rectangle(1, 2, 0, 1)
        rd4 = Rectangle(2, 2, 1, 1)

    def test_0(self):
        rd1 = Rectangle(2, 1, 0 ,0)
        self.assertEqual(rd1.display(), None) 

if __name__ == '__main__':
    unittest.main()
