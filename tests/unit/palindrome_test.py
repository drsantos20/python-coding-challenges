import unittest

from arcade.palindrome_challenge import Palindrome


class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.test_palindrome = Palindrome

    def test_palindrome(self):
        self.assertIs(True, self.test_palindrome.check_palindrome('a'))
        self.assertIs(True, self.test_palindrome.check_palindrome('aabaa'))
        self.assertIs(True, self.test_palindrome.check_palindrome('aacbcaa'))
        self.assertIs(False, self.test_palindrome.check_palindrome('ab'))
        self.assertIs(False, self.test_palindrome.check_palindrome('aaxbcaa'))
        self.assertIs(False, self.test_palindrome.check_palindrome('aabcaabc'))
