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
