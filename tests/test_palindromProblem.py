import unittest

from palindromProblem import palindrom

class test_palindromProblem(unittest.TestCase):
    def test_can_check_palindrom_word(self):
        """
        Test that it can check palindrom word
        """
        word = "KATAK"
        result = palindrom(word)
        self.assertTrue(result)

    def test_can_check_empty_string(self):
        """
        Test that it can check empty string
        """
        word = ""
        result = palindrom(word)
        self.assertFalse(result)

    def test_can_check_non_palindrom_word(self):
        """
        Test that it can check non palindrom word
        """
        word = "KATAKI"
        result = palindrom(word)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()