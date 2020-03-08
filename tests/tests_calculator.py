import unittest

from calculator.calculator import Calculator


class TestCases(unittest.TestCase):
	def setUp(self):
		self.calculator = Calculator()

	def test_instantiation(self):
		self.assertIsInstance(self.calculator, Calculator)

	def test_addition(self):
		self.assertEqual(5, self.calculator.addition(2, 3))

	def test_addition_list(self):
		self.assertEqual(11, self.calculator.addition([2, 3, 6]))

	def test_subtraction(self):
		self.assertEqual(3, self.calculator.subtraction(6, 3))

	def test_multiplication(self):
		self.assertEqual(12, self.calculator.multiplication(3, 4))

	def test_division(self):
		self.assertEqual(3.5, self.calculator.division(7, 2))

	def test_exponentiation(self):
		self.assertEqual(27, self.calculator.exponentiation(3, 3))

	def test_nthroot(self):
		self.assertEqual(4, self.calculator.nthroot(16, 2))

	def test_logarithm(self):
		self.assertEqual(3, self.calculator.logarithm(8, 2))
