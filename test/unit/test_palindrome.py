import unittest

from arcade.palindrome_challenge import Palindrome


class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.palindrome = Palindrome()

    def test_palindrome(self):
        self.assertTrue(self.palindrome.check_palindrome('a'))
        self.assertTrue(self.palindrome.check_palindrome('aabaa'))
        self.assertTrue(self.palindrome.check_palindrome('aacbcaa'))
        self.assertFalse(self.palindrome.check_palindrome('ab'))
        self.assertFalse(self.palindrome.check_palindrome('aaxbcaa'))
        self.assertFalse(self.palindrome.check_palindrome('aabcaabc'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPalindrome)
    unittest.TextTestRunner(verbosity=2).run(suite)
