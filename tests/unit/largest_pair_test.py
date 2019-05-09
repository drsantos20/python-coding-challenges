import unittest

from arcade.largest_pair import LargestPair


class TestLargestPair(unittest.TestCase):

    def setUp(self):
        self.test_largest_pair = LargestPair

    def test_largest_pair(self):
        self.assertEqual(21, self.test_largest_pair.adjacent_elements_product([3, 6, -2, -5, 7, 3]))
