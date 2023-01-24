# Abstract Factory : pet factory
# Concrete Factory : dog factory and cat factory
# Concrete Product : Dog and dog food, Cat and cat food

class Dog:
	"""One of the objects to be returned"""

	def speak(self):
		return "woof!"

	def __str__(self):
		return "Dog"

class DogFactory:
	"""Concrete Factory"""

	def get_pet(self):
		return Dog()

	def get_food(self):
		return "Dog Food"

class Cat:
	"""One of the objects to be returned"""

	def speak(self):
		return "meow!"

	def __str__(self):
		return "Cat"

class CatFactory:
	"""Concrete Factory"""

	def get_pet(self):
		return Cat()

	def get_food(self):
		return "Cat Food"

class PetStore:
	"""PetStore houses our abstract factory"""

	def __init__(self, pet_factory=None):
		"""pet_factory is our abstract factory"""
		self._pet_factory = pet_factory

	def show_pet(self):
		"""Utility method to display the details of the objects returned"""

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is {}".format(pet))
		print("Our pet says {}".format(pet.speak()))
		print("Its food is {}".format(pet_food))

#####################################################

factory1 = DogFactory()
factory2 = CatFactory()

shop = PetStore(factory1)
shop.show_pet()
