#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unit testing of 6-max_integer module"""
    def test_max_result(self):
        """ Test to get maximum result for positive and
        negative lists of integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -5, -10, -2]), -1)
        self.assertEqual(max_integer([-2, 4, -8, 15]), 15)

    def test_return_none(self):
        """Test to check that None is returned when no argument is given
        or when an empty list is given
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_more_arguments(self):
        """Test to check for case of more the required number of arguments"""
        test_list_1 = [5, 6, 7]
        test_list_2 = [11, 13, 21, 4]

        self.assertRaises(TypeError, max_integer, test_list_1, test_list_2)

    def test_one_element(self):
        """Test to check if correct result is returned for one element list"""
        self.assertEqual(max_integer([17]), 17)
