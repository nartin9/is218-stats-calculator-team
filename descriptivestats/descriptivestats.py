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

		mid = len(sortedData) // 2

		if len(sortedData) & 1 == 1:
			return sortedData[mid]

		return (sortedData[mid - 1] + sortedData[mid]) / 2
