# Factory
# Let's suppose our pet shop sells dogs currently. Now we need to add a new pet i.e, a cat

class Dog:
	"""A simple dog class"""

	def __init__(self, name):
		self.name = name

	def speak(self):
		return "woof!"

class Cat:
	"""A simple cat class"""

	def __init__(self, name):
		self.name = name

	def speak(self):
		return "meow!"

#################################################

def get_pet(pet="dog"):
	"""The Factory Method"""

	pets = dict(dog=Dog('Sheru'), cat=Cat('Kitty'))
	return pets[pet]

print(get_pet("dog").speak())
print(get_pet("cat").speak())