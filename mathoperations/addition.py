class Addition:
	def __init__(self):
		pass

	@staticmethod
	def sum(augend, addend=None):
		if type(augend) == list:
			total = 0
			for x in augend:
				total += x
		else:
			total = augend + addend

		return total
