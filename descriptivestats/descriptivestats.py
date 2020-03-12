import math


class DescriptiveStatistics:
	def __init__(self):
		pass

	@staticmethod
	def mean(data):
		return sum(data) / len(data)

	@staticmethod
	def median(data):
		sortedData = data[:]
		sortedData.sort()

		return DescriptiveStatistics._median(sortedData)["median"]

	@staticmethod
	def mode(data):
		count = {}
		maxCount = 0

		for d in data:
			if d not in count:
				count[d] = 0
			count[d] += 1

			if count[d] > maxCount:
				maxCount = count[d]

		largest = []

		for k, v in count.items():
			if v == maxCount:
				largest.append(k)

		largest.sort()
		return largest

	"""sample standard deviation"""
	@staticmethod
	def stdev(data):
		mean = DescriptiveStatistics.mean(data)
		total = 0

		for d in data:
			total += (d - mean) ** 2

		return math.sqrt(total / (len(data) - 1))

	"""sample variance"""
	@staticmethod
	def variance(data):
		return DescriptiveStatistics.stdev(data) ** 2

	@staticmethod
	def quartiles(data):
		sortedData = data[:]
		sortedData.sort()

		quar2 = DescriptiveStatistics._median(sortedData)
		quar1 = DescriptiveStatistics._median(sortedData[:quar2["end1idx"] + 1])
		quar3 = DescriptiveStatistics._median(sortedData[quar2["start2idx"]:])

		return [quar1["median"], quar2["median"], quar3["median"]]

	@staticmethod
	def skewness(data):
		return 3 * (DescriptiveStatistics.mean(data) - DescriptiveStatistics.median(data)) / DescriptiveStatistics.stdev(data)

	@staticmethod
	def zscore(value, mean, stdev):
		return (value - mean) / stdev

	@staticmethod
	def meanDeviation(data):
		mean = DescriptiveStatistics.mean(data)
		absdiff = []

		for d in data:
			absdiff.append(abs(d - mean))

		return DescriptiveStatistics.mean(absdiff)

	"""assumes data is already sorted"""
	@staticmethod
	def _median(data):
		mid = len(data) // 2

		end1idx = mid - 1

		if len(data) & 1 == 1:
			median = data[mid]
			start2idx = mid + 1
		else:
			median = (data[mid - 1] + data[mid]) / 2
			start2idx = mid

		return {
			"median": median,
			"end1idx": end1idx,
			"start2idx": start2idx
		}
