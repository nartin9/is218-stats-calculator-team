import unittest

from descriptivestats.descriptivestats import DescriptiveStatistics


class TestCases(unittest.TestCase):
	def setUp(self):
		pass

	def test_mean(self):
		lst = [3, 2, 6, 1, 8]
		self.assertEqual(4, DescriptiveStatistics.mean(lst))
