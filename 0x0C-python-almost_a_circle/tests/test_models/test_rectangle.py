#!/usr/bin/python3
from contextlib import redirect_stdout
import inspect
import io
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
import json
from io import StringIO
import sys

'''
    Runs test cases for the Rectangle module
'''


class test_rectangle(unittest.TestCase):
    '''
    Testing rectangle
    '''

    def setUp(self):
        '''
        Initializing instance with width and height
        parameters
        '''
        self.r = Rectangle(5, 10)

    def tearDown(self):
        '''
        Deleting created instance
        '''
        del self.r

    def test_width(self):
        '''
        Testing the Rectangle width getter
        '''
        self.assertEqual(5, self.r.width)


if __name__ == "__main__":
    unittest.main()
