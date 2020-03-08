import unittest

from calculator.calculator import Calculator


class TestCases(unittest.TestCase):
	def setUp(self):
		self.calculator = Calculator()

	def test_instantiation(self):
		self.assertIsInstance(self.calculator, Calculator)
