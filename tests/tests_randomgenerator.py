import unittest

from randomgenerator.randomgenerator import RandomGenerator


class TestCases(unittest.TestCase):
	def setUp(self):
		pass
	def test_rangeInt(self):
		random.seed(1)
		self.assertEqual(4, RandomGenerator.rangeInt(2,10))
	def test_rangeDec(self):
		random.seed(1)
		self.assertEqual(3.0749139528992098, RandomGenerator.uniform(2,10))
	def test_rangeIntSeeded(self):
		self.assertEqual(4, RandomGenerator.rangeInt(2,10,1))
	def test_rangeDecSeeded(self):
		self.assertEqual(3.0749139528992098, RandomGenerator.uniform(2,10,1))
	def test_choose(self):
		random.seed(1)
		elements = [1,2,3,"A","B"] 
		self.assertEqual(2,RandomGenerator.choose(elements))
	def test_chooseN(self):
		random.seed(1)
		elements = [1,2,3,"A","B"] 
		self.assertEqual([2, 'B', 1],RandomGenerator.choose(elements))
	def test_chooseNSeeded(self):
		elements = [1,2,3,"A","B"] 
		self.assertEqual([2, 'B', 1],RandomGenerator.choose(elements))
	
	
