class Fraction():
	def __init__(self, num, denom):
		self.num = num
		self.denom = denom
	
	def __add__(self, other):
		return Fraction((self.num*other.denom) + (other.num*self.denom), self.denom * other.denom)
	
	def __sub__(self, other):
		return Fraction((self.num*other.denom) - (other.num*self.denom), self.denom * other.denom)
		
	def __mul__(self, other):
		return Fraction(self.num * other.num, self.denom * other.denom)
	#__div__ doesn't work, needs to be truediv t
	def __truediv__(self, other):
		return Fraction(self.num * other.denom, self.denom * other.num)
		
	def inverse(self):
		return Fraction(self.denom, self.num)
		
	def __str__(self):
		return "" + str(self.num) + "/" + str(self.denom)

fr1 = Fraction(1, 5)
fr2 = Fraction(4, 10)
print(fr1/fr2)