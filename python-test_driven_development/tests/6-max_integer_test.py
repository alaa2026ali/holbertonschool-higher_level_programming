#!/usr/bin/python3
"""Module to test max_integer function using unittest."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_max_at_beginning(self):
        """Test with the maximum value at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_end(self):
        """Test with the maximum value at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test with the maximum value in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative(self):
        """Test with a list containing one negative number."""
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_all_negative(self):
        """Test with a list where all numbers are negative."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        """Test with a list that has only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list (should return None)."""
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
