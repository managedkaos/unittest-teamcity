"""
This is a test suite for the main function.
"""
import unittest
from main import target


class TestMainFunction(unittest.TestCase):
    """
    This class contains test cases for the main function.
    """

    def test_main_positive(self):
        """
        Test cases for positive integers.
        """
        self.assertEqual(target(3), 9)
        self.assertEqual(target(4), 16)
        self.assertEqual(target(10), 100)

    def test_main_zero(self):
        """
        Test case for zero.
        """
        self.assertEqual(target(0), 0)

    def test_main_negative(self):
        """
        Test cases for negative integers.
        """
        self.assertEqual(target(-2), 4)
        self.assertEqual(target(-5), 25)


if __name__ == '__main__':
    unittest.main()
