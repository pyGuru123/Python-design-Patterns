class House:
	# The class being visited

	def accept(self, visitor):
		"""Interface to accept a visitor"""
		visitor.visit(self) # Triggers the visiting operation


	def work_on_havc(self, hvac_specialist):
		print(self, "worked on by", hvac_specialist)

	def work_on_electricity(self, electrician):
		print(self, "worked on by", electrician)

	def __str__(self):
		"""Simply return the class name when house is being printed"""
		return self.__class__.__name__

class Visitor:
	"""Abstract Visitor"""
	def __str__(self):
		"""Simply return the class name when Visitor object is printed"""
		return self.__class__.__name__

class HvacSpecialist(Visitor):
	"""Concrete Visitor : hvac specialist"""
	def visit(self, house):
		house.work_on_havc(self)

class Electrician(Visitor):
	"""Concrete Visitor: electrician"""
	def visit(self, house):
		house.work_on_electricity(self)

hvac = HvacSpecialist()
electrician = Electrician()
house = House()

house.accept(hvac)
house.accept(electrician)
print(house)