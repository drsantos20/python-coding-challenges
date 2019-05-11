import unittest

from arcade.largest_increasing_sequence import LargestIncreasingSequence


class TestLargestIncreasingSequence(unittest.TestCase):

    def setUp(self):
        self.largest_increasing_sequence = LargestIncreasingSequence()

    def test_almost_increasing_sequence(self):
        self.assertFalse(self.largest_increasing_sequence.almost_increasing_sequence([1, 3, 2, 1]))
        self.assertTrue(self.largest_increasing_sequence.almost_increasing_sequence([1, 3, 2]))
        self.assertFalse(self.largest_increasing_sequence.almost_increasing_sequence([40, 50, 60, 10, 20, 30]))
