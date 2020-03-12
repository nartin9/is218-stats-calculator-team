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

	def test_stdev(self):
		data = [22, 56, 12, 32, 65, 15]
		self.assertAlmostEqual(22.0786473, DescriptiveStatistics.stdev(data))

	def test_pstdev(self):
		data = [22, 56, 12, 32, 65, 15]
		self.assertAlmostEqual(20.15495527, DescriptiveStatistics.pstdev(data))

	def test_variance(self):
		data = [22, 56, 12, 32, 65, 15]
		self.assertAlmostEqual(487.46666666, DescriptiveStatistics.variance(data))

	def test_covariance(self):
		data1 = [14.2, 16.4, 11.9, 15.2, 18.5]
		data2 = [215, 325, 185, 332, 406]

		self.assertEqual(211.445, DescriptiveStatistics.covariance(data1, data2))

	def test_pcovariance(self):
		data1 = [14.2, 16.4, 11.9, 15.2, 18.5]
		data2 = [215, 325, 185, 332, 406]

		self.assertEqual(169.156, DescriptiveStatistics.pcovariance(data1, data2))

	def test_quartiles_odd(self):
		data = [9, 8, 2, 5, 2, 1, 12]
		self.assertEqual([2, 5, 9], DescriptiveStatistics.quartiles(data))

	def test_quartiles_even(self):
		data = [9, 8, 2, 5, 2, 1, 12, 15]
		self.assertEqual([2, 6.5, 10.5], DescriptiveStatistics.quartiles(data))

	def test_skewness(self):
		data = [22, 56, 12, 32, 65, 15]
		self.assertAlmostEqual(0.90585259, DescriptiveStatistics.skewness(data))

	def test_zscore(self):
		value = 1100
		mean = 1026
		stdev = 209
		self.assertAlmostEqual(0.35406698, DescriptiveStatistics.zscore(value, mean, stdev))

	def test_meanDeviation(self):
		data = [3, 2, 6, 1, 8]
		self.assertEqual(2.4, DescriptiveStatistics.meanDeviation(data))

	def test_sample_correlation(self):
		data1 = [14.2, 16.4, 11.9, 15.2, 18.5]
		data2 = [215, 325, 185, 332, 406]

		self.assertAlmostEqual(0.94532854, DescriptiveStatistics.sampleCorrelation(data1, data2))

	def test_population_correlation(self):
		data1 = [14.2, 16.4, 11.9, 15.2, 18.5]
		data2 = [215, 325, 185, 332, 406]

		self.assertAlmostEqual(0.94532854, DescriptiveStatistics.populationCorrelation(data1, data2))
