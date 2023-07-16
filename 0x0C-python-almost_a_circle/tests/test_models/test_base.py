#!/usr/bin/python3

import unittest
from models.base import Base


'''
    Creating test cases for the base module
'''


class TestBase(unittest.TestCase):
    """
        Test cases for the Base class.
            """

    def test_id_assignment(self):
        """
        Test that each instance of Base has a unique id assigned.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """
        Test that Base assigns the provided id if given.
        """
        b3 = Base(10)
        self.assertEqual(b3.id, 10)


if __name__ == '__main__':
    unittest.main()
