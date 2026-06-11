#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test list of negative numbers"""
        self.assertEqual(max_integer([-5, -2, -9, -1]), -1)

    def test_single_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_all_equal(self):
        """Test list with equal values"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """Test list of floats"""
        self.assertEqual(max_integer([1.5, 3.2, 2.8]), 3.2)

    def test_mixed_int_float(self):
        """Test mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_list_of_one_negative(self):
        """Test single negative value"""
        self.assertEqual(max_integer([-10]), -10)

    def test_string_list(self):
        """Test list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_string_argument(self):
        """Test string argument"""
        self.assertEqual(max_integer("hello"), "o")

    def test_mixed_numbers(self):
        """Test mixed positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)


if __name__ == "__main__":
    unittest.main()
