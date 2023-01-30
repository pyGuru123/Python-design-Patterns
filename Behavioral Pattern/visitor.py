class House:
	# The class being visited

	def accept(self, visitor):
		"""Interface to accept a visitor"""
		# Triggers the visiting operation


	def work_on_havc(self, hvac_specialist):
		print(self, "worked on by", hvac_specialist)

	def work_on_electricity(self, electrician):
		print(self, "worked on by", electrician)

	def __str__(self):
		"""Simply return the class name when house is being printed"""
		return self.__class__.__name__