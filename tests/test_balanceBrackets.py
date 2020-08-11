import unittest

from balanceBrackets import balanceBrackets

class TestBalanceBracket(unittest.TestCase):
    def test_bb_empty_list(self):
        """
        Test that it can check empty list
        """
        brackets = []
        result = balanceBrackets(brackets)
        self.assertEqual(result, -1)

    def test_bb_is_balance(self):
        """
        Test that it can check balance bracket
        """
        brackets = "(){}"
        result = balanceBrackets(brackets)
        self.assertEqual(result, "balance")

    def test_bb_is_unbalance(self):
        """
        Test that it can check unbalance bracket
        """
        brackets = "(){}["
        result = balanceBrackets(brackets)
        self.assertEqual(result, "unbalance")

    def test_bb_balance_symetric(self):
        """
        Test that it can check balance bracket with symetrical form
        """
        brackets = "{([()])}"
        result = balanceBrackets(brackets)
        self.assertEqual(result, "balance")

    def test_bb_unbalance_odd_brackets(self):
        """
        Test that it can check unbalance bracket with odd bracket
        """
        brackets = "{}("
        result = balanceBrackets(brackets)
        self.assertEqual(result, "unbalance")

if __name__ == "__main__":
    unittest.main()