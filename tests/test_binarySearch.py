import unittest

from binarysearch import binary

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_most_left(self):
        """
        Test that it can find most left number
        """
        items = [1,2,3,4,5,6,7]
        target = 1
        result = binary(items, target)
        self.assertTrue(result)

    def test_binary_search_most_right(self):
        """
        Test that it can find most right number
        """
        items = [1,2,3,4,5,6,7]
        target = 7
        result = binary(items, target)
        self.assertTrue(result)

    def test_binary_search_in_middle_number(self):
        """
        Test that it can find number in the middle
        """
        items = [1,2,3,4,5,6,7]
        target = 4
        result = binary(items, target)
        self.assertTrue(result)

    def test_binary_search_in_very_long_list(self):
        """
        Test that it can find number in very long list
        """
        items = list(range(10000))
        target = 1263
        result = binary(items, target)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()