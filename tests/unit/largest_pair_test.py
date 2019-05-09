import unittest

from arcade.largest_pair import LargestPair


class TestLargestPair(unittest.TestCase):

    def setUp(self):
        self.test_largest_pair = LargestPair

    def test_largest_pair(self):
        self.assertEqual(21, self.test_largest_pair.adjacent_elements_product([3, 6, -2, -5, 7, 3]))
        self.assertEqual(2, self.test_largest_pair.adjacent_elements_product([-1, -2]))
        self.assertEqual(6, self.test_largest_pair.adjacent_elements_product([5, 1, 2, 3, 1, 4]))
        self.assertEqual(6, self.test_largest_pair.adjacent_elements_product([1, 2, 3, 0]))
        self.assertEqual(50, self.test_largest_pair.adjacent_elements_product([9, 5, 10, 2, 24, -1, -48]))
        self.assertEqual(-12, self.test_largest_pair.adjacent_elements_product([-23, 4, -3, 8, -12]))
