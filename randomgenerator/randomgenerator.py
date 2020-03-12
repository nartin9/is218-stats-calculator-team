import random

class RandomGenerator:
	def __init__(self):
		pass

def rangeInt(x,y):
    return random.randint(x, y)

def rangeDec(x,y):
    return random.uniform(a,b)

def rangeIntSeeded(x, y, z);
    random.seed(z)
    return random.randint(x, y)

def rangeDecSeeded(x, y, z);
    random.seed(z)
    return random.uniform(x, y)

def rangeListSeeded(x, y, z)
    nums = []
    for i in range(0, z):
        nums.append(random.randint(x, y))
    return nums

def choose(elements);
    return random.choice(elements)

def chooseN(elements, n);
    values = []
    for x in range(n):
        values.append(random.choice(elements))

//elements: a list      n: number of elements       s: the seed
def ChooseNSeeded(elements, n, s)
    random.seed(s)
    values = []
    for x in range(n):
        values.append(random.choice(elements))
