from mathoperations.addition import Addition
from mathoperations.subtraction import Subtraction
from mathoperations.multiplication import Multiplication
from mathoperations.division import Division
from mathoperations.exponentiation import Exponentiation
from mathoperations.nthroot import NthRoot
from mathoperations.logarithm import Logarithm


class Calculator:
	def __init__(self):
		self.result = None
	# result = x+y
	def addition(self, x, y=None):
		self.result = Addition.sum(x, y)
		return self.result
	#result= x-y	
	def subtraction(self, x, y):
		self.result = Subtraction.difference(x, y)
		return self.result
	#result= x*y
	def multiplication(self, x, y):
		self.result = Multiplication.product(x, y)
		return self.result
	#result= x/y
	def division(self, x, y):
		self.result = Division.quotient(x, y)
		return self.result
	# result = x^y	
	def exponentiation(self, x, y):
		self.result = Exponentiation.power(x, y)
		return self.result
	# result= x to the y root
	def nthroot(self, x, y):
		self.result = NthRoot.root(x, y)
		return self.result
	# result = logarithm base x of y	
	def logarithm(self, x, y):
		self.result = Logarithm.logarithm(x, y)
		return self.result
