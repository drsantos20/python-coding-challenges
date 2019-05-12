import unittest

from arcade.time_convert import TimeConvert


class TestTimeConvert(unittest.TestCase):

    def setUp(self):
        self.time_convert = TimeConvert()

    def test_time_convert(self):
        self.assertEqual('2:6', self.time_convert.time_convert(num=126))
        self.assertEqual('0:45', self.time_convert.time_convert(num=45))
        self.assertEqual('1:0', self.time_convert.time_convert(num=60))
