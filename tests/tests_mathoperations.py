import unittest

from mathoperations.addition import Addition
from mathoperations.subtraction import Subtraction


class TestCases(unittest.TestCase):
	def setUp(self):
		pass

	def test_sum(self):
		self.assertEqual(5, Addition.sum(2, 3))

	def test_sum_list(self):
		self.assertEqual(11, Addition.sum([2, 3, 6]))

	def test_difference(self):
		self.assertEqual(3, Subtraction.difference(6, 3))
