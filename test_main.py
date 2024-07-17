"""
This is a test suite for the main function.
"""
import unittest
import main


class TestMainFunction(unittest.TestCase):
    """
    This class contains test cases for the main function.
    """

    def test_main_positive(self):
        """
        Test cases for positive integers.
        """
        self.assertEqual(main(3), 9)
        self.assertEqual(main(4), 16)
        self.assertEqual(main(10), 100)

    def test_main_zero(self):
        """
        Test case for zero.
        """
        self.assertEqual(main(0), 0)

    def test_main_negative(self):
        """
        Test cases for negative integers.
        """
        self.assertEqual(main(-2), 4)
        self.assertEqual(main(-5), 25)


if __name__ == '__main__':
    unittest.main()

