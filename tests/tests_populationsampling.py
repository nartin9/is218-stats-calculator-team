import unittest
import random

from populationsampling.populationsampling import PopulationSampling


class TestCases(unittest.TestCase):
	def setUp(self):
		pass

	def test_simpleRandomSampling(self):
		data = [1, 4, 7, 2, 7, 3, 8, 5]

		random.seed(152)
		self.assertEqual([6, 5, 1], PopulationSampling.simpleRandomSampling(data, 3))

	def test_systematicSampling(self):
		data = [1, 4, 7, 2, 7, 3, 8, 5]

		random.seed(152)
		self.assertEqual([8, 1, 7], PopulationSampling.systematicSampling(data, 3))

	def test_marginOfError(self):
		self.assertAlmostEqual(0.02193138, PopulationSampling.marginOfError(0.4, 900, 0.95))

	def test_cochranSampleSize(self):
		self.assertAlmostEqual(385, PopulationSampling.cochranSampleSize(0.5, 0.95, 0.05))

	def test_findSampleSize(self):
		self.assertAlmostEqual(224, PopulationSampling.findSampleSize(2.9, 0.99, 0.5))
