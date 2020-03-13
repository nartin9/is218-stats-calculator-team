import unittest
import random

from populationsampling.populationsampling import PopulationSampling

from randomgenerator.randomdata import RandomData


class TestCases(unittest.TestCase):
	def setUp(self):
		self.testdata = RandomData(12345).list(0, 1000.0, 20)

	def test_simpleRandomSampling(self):
		random.seed(152)
		self.assertEqual([553.2210855693298, 368.4116894884757, 958.0647850995487], PopulationSampling.simpleRandomSampling(self.testdata, 3))

	def test_systematicSampling(self):
		random.seed(152)
		self.assertEqual([553.2210855693298, 503.9353681100375, 368.4116894884757], PopulationSampling.systematicSampling(self.testdata, 3))

	def test_confidenceInterval(self):
		r = PopulationSampling.confidenceInterval(self.testdata, 0.95)
		self.assertAlmostEqual(406.71759600, r[0])
		self.assertAlmostEqual(299.31429363, r[1])
		self.assertAlmostEqual(514.12089838, r[2])

	def test_marginOfError(self):
		self.assertAlmostEqual(0.02193138, PopulationSampling.marginOfError(0.4, 900, 0.95))

	def test_cochranSampleSize(self):
		self.assertAlmostEqual(385, PopulationSampling.cochranSampleSize(0.5, 0.95, 0.05))

	def test_findSampleSize(self):
		self.assertAlmostEqual(224, PopulationSampling.findSampleSize(2.9, 0.99, 0.5))
