import unittest

from arcade.largest_pair import LargestPair


class TestLargestPair(unittest.TestCase):

    def setUp(self):
        self.largest_pair = LargestPair()

    def test_largest_pair(self):
        self.assertEqual(21, self.largest_pair.adjacent_elements_product([3, 6, -2, -5, 7, 3]))
        self.assertEqual(2, self.largest_pair.adjacent_elements_product([-1, -2]))
        self.assertEqual(6, self.largest_pair.adjacent_elements_product([5, 1, 2, 3, 1, 4]))
        self.assertEqual(6, self.largest_pair.adjacent_elements_product([1, 2, 3, 0]))
        self.assertEqual(50, self.largest_pair.adjacent_elements_product([9, 5, 10, 2, 24, -1, -48]))
        self.assertEqual(-12, self.largest_pair.adjacent_elements_product([-23, 4, -3, 8, -12]))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLargestPair)
    unittest.TextTestRunner(verbosity=2).run(suite)
