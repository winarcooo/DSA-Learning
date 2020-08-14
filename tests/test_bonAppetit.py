import unittest

from bonAppetit import bonAppetit

class TestBonAppetit(unittest.TestCase):
    def test_ba_brian_case_1(self):
        """
        Test that brian own to anna 5
        """
        bill = [3,10,2,9]
        b = 12
        k = 1
        result = bonAppetit(bill, k, b)
        self.assertEqual(result, 5)
    
    def test_ba_case_two(self):
        """
        Test that no own and bon appetite
        """
        bill = [3,10,2,9]
        b = 7
        k = 1
        result = bonAppetit(bill, k, b)
        self.assertEqual(result, 'Bon Appetit')

if __name__ == '__main__':
    unittest.main()