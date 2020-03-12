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

	@staticmethod
	def quartiles(data):
		sortedData = data[:]
		sortedData.sort()

		quar2 = DescriptiveStatistics._median(sortedData)
		quar1 = DescriptiveStatistics._median(sortedData[:quar2["end1idx"] + 1])
		quar3 = DescriptiveStatistics._median(sortedData[quar2["start2idx"]:])

		return [quar1["median"], quar2["median"], quar3["median"]]

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
