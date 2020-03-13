import random


class RandomData:
	def __init__(self, seed):
		self.seed = seed

		random.seed(self.seed)

	def list(self, x, y, n):
		data = []

		for i in range(n):
			data.append(self.range(x, y))

		return data

	def range(self, x, y):
		if type(x) == int and type(y) == int:
			return random.randrange(x, y)
		return random.random() * (y - x) + x
