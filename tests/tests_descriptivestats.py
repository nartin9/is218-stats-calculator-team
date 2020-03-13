import unittest

from descriptivestats.descriptivestats import DescriptiveStatistics

from randomgenerator.randomdata import RandomData


class TestCases(unittest.TestCase):
	def setUp(self):
		self.testdata = RandomData(12345).list(0, 1000.0, 20)

	def test_mean(self):
		self.assertAlmostEqual(406.71759600, DescriptiveStatistics.mean(self.testdata))

	def test_median(self):
		self.assertAlmostEqual(390.26554121, DescriptiveStatistics.median(self.testdata))

	def test_mode_single(self):
		data = [1, 7, 4, 7, 2, 8]
		self.assertEqual([7], DescriptiveStatistics.mode(data))

	def test_mode_multiple(self):
		data = [1, 7, 4, 7, 2, 8, 4]
		self.assertEqual([4, 7], DescriptiveStatistics.mode(data))

	def test_stdev(self):
		self.assertAlmostEqual(277.78211542, DescriptiveStatistics.stdev(self.testdata))

	def test_pstdev(self):
		self.assertAlmostEqual(270.74851517, DescriptiveStatistics.pstdev(self.testdata))

	def test_variance(self):
		self.assertAlmostEqual(77162.90365125, DescriptiveStatistics.variance(self.testdata))

	def test_covariance(self):
		data1 = [14.2, 16.4, 11.9, 15.2, 18.5]
		data2 = [215, 325, 185, 332, 406]

		self.assertEqual(211.445, DescriptiveStatistics.covariance(data1, data2))

	def test_pcovariance(self):
		data1 = [14.2, 16.4, 11.9, 15.2, 18.5]
		data2 = [215, 325, 185, 332, 406]

		self.assertEqual(169.156, DescriptiveStatistics.pcovariance(data1, data2))

	def test_quartiles(self):
		self.assertEqual([168.01569232654998, 390.26554121388835, 557.6497868225864], DescriptiveStatistics.quartiles(self.testdata))

	def test_skewness(self):
		self.assertAlmostEqual(0.17767941, DescriptiveStatistics.skewness(self.testdata))

	def test_zscore(self):
		value = 1100
		mean = 1026
		stdev = 209
		self.assertAlmostEqual(0.35406698, DescriptiveStatistics.zscore(value, mean, stdev))

	def test_meanDeviation(self):
		self.assertAlmostEqual(214.16539738, DescriptiveStatistics.meanDeviation(self.testdata))

	def test_sample_correlation(self):
		data1 = [14.2, 16.4, 11.9, 15.2, 18.5]
		data2 = [215, 325, 185, 332, 406]

		self.assertAlmostEqual(0.94532854, DescriptiveStatistics.sampleCorrelation(data1, data2))

	def test_population_correlation(self):
		data1 = [14.2, 16.4, 11.9, 15.2, 18.5]
		data2 = [215, 325, 185, 332, 406]

		self.assertAlmostEqual(0.94532854, DescriptiveStatistics.populationCorrelation(data1, data2))
