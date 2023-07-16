#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_id_assignment(self):
        """
        Test that each instance of Rectangle has a unique id assigned.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def test_custom_id(self):
        """
        Test that Rectangle assigns the provided id if given.
        """
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_attributes(self):
        """
        Test that the attributes of Rectangle are assigned correctly.
        """
        r4 = Rectangle(5, 5, 1, 2, 7)
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 5)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 2)

        r4.width = 10
        r4.height = 3
        r4.x = 2
        r4.y = 4

        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 3)
        self.assertEqual(r4.x, 2)
        self.assertEqual(r4.y, 4)


if __name__ == '__main__':
    unittest.main()
