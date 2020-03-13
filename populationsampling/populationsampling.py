import math
import random

import scipy.stats

from descriptivestats.descriptivestats import DescriptiveStatistics


class PopulationSampling:
	def __init__(self):
		pass
	
	@staticmethod # data is a list  n is the number of samples you want to take
	def simpleRandomSampling(data, n):
		if len(data) == 0:
			raise Exception("list is empty")

		sample = []

		for i in range(n):
			r = random.randrange(0, len(data))
			sample.append(data[r])

			#without replacement
			data = data[:r] + data[r + 1:]

		return sample

	@staticmethod # data is a list  n is the number of samples you want to take
	def systematicSampling(data, n):
		if len(data) == 0:
			raise Exception("list is empty")
		if n == 0:
			raise ZeroDivisionError()

		sample = []
		k = len(data) // n

		idx = random.randrange(0, len(data))
		for i in range(n):
			sample.append(data[idx])

			idx += k
			if idx >= len(data):
				idx -= len(data)

		return sample

	@staticmethod # data is a list  
	def confidenceInterval(data, confidence):
		if len(data) == 0:
			raise Exception("list is empty")

		mean = DescriptiveStatistics.mean(data)
		se = scipy.stats.sem(data)
		i = se * PopulationSampling.tscore(len(data), confidence)
		return [mean, mean - i, mean + i]

	@staticmethod
	def marginOfError(pstdev, n, confidenceLevel):
		if n == 0:
			raise ZeroDivisionError()

		zscore = scipy.stats.norm.ppf(confidenceLevel)
		return zscore * pstdev / math.sqrt(n)

	@staticmethod
	def cochranSampleSize(p, confidenceLevel, precision):
		if precision == 0:
			raise ZeroDivisionError()

		zscore = scipy.stats.norm.ppf(confidenceLevel + (1 - confidenceLevel) / 2)
		return math.ceil((zscore ** 2) * p * (1 - p) / (precision ** 2))

	@staticmethod
	def findSampleSize(stdev, confidenceLevel, precision):
		if precision == 0:
			raise ZeroDivisionError()

		zscore = scipy.stats.norm.ppf(confidenceLevel + (1 - confidenceLevel) / 2)
		return math.ceil((zscore * stdev / precision) ** 2)

	@staticmethod
	def tscore(n, confidence):
		return scipy.stats.t.ppf(confidence, n - 1)
