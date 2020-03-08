import unittest

from mathoperations.addition import Addition
from mathoperations.subtraction import Subtraction
from mathoperations.multiplication import Multiplication
from mathoperations.division import Division
from mathoperations.exponentiation import Exponentiation
from mathoperations.nthroot import NthRoot
from mathoperations.logarithm import Logarithm


class TestCases(unittest.TestCase):
	def setUp(self):
		pass

	def test_sum(self):
		self.assertEqual(5, Addition.sum(2, 3))

	def test_sum_list(self):
		self.assertEqual(11, Addition.sum([2, 3, 6]))

	def test_difference(self):
		self.assertEqual(3, Subtraction.difference(6, 3))

	def test_product(self):
		self.assertEqual(12, Multiplication.product(3, 4))

	def test_quotient(self):
		self.assertEqual(3.5, Division.quotient(7, 2))
		
	def test_power(self):
		self.assertEqual(27, Exponentiation.power(3, 3))

	def test_root(self):
		self.assertEqual(4, NthRoot.root(16, 2))

	def test_logarithm(self):
		self.assertEqual(3, Logarithm.logarithm(8, 2))