import unittest

from descriptivestats.descriptivestats import DescriptiveStatistics


class TestCases(unittest.TestCase):
	def setUp(self):
		pass

	def test_mean(self):
		data = [3, 2, 6, 1, 8]
		self.assertEqual(4, DescriptiveStatistics.mean(data))

	def test_median_odd(self):
		data = [3, 2, 6, 1, 8]
		self.assertEqual(3, DescriptiveStatistics.median(data))

	def test_median_even(self):
		data = [3, 2, 6, 1, 8, 4]
		self.assertEqual(3.5, DescriptiveStatistics.median(data))

	def test_mode_single(self):
		data = [1, 7, 4, 7, 2, 8]
		self.assertEqual([7], DescriptiveStatistics.mode(data))

	def test_mode_multiple(self):
		data = [1, 7, 4, 7, 2, 8, 4]
		self.assertEqual([4, 7], DescriptiveStatistics.mode(data))
