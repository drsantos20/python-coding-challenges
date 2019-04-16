import unittest

from arcade.palindrome_challenge import Arcade


class TestArcade(unittest.TestCase):

    def setUp(self):
        self.test_palindrome = Arcade

    def test_palindrome(self):
        self.assertIs(True, self.test_palindrome.checkPalindrome('a'))
        self.assertIs(True, self.test_palindrome.checkPalindrome('aabaa'))
        self.assertIs(True, self.test_palindrome.checkPalindrome('aacbcaa'))
        self.assertIs(False, self.test_palindrome.checkPalindrome('ab'))
        self.assertIs(False, self.test_palindrome.checkPalindrome('aaxbcaa'))
        self.assertIs(False, self.test_palindrome.checkPalindrome('aabcaabc'))
