# A prototype class has 4 different methods.

import copy

class Prototype:
	"""The Prototype design pattern"""

	def __init__(self):
		self._objects = {}

	def register_object(self, name, obj):
		"""Register an object"""
		self._objects[name] = obj

	def unregister_object(self, name):
		"""Unregister an object"""
		del self._objects[name]

	def clone(self, name, **attr):
		"""Clone a registered object and update its attributes"""
		obj = copy.deepcopy(self._objects.get(name))
		obj.__dict__.update(attr)
		return obj

class Car:
	def __init__(self):
		self.name = 'SkyLark'
		self.color = "red"
		self.options = "Ex"

	def __str__(self):
		return '{} | {} | {}'.format(self.name, self.color, self.options)

car = Car()
prototype = Prototype()
prototype.register_object('skylark', car)

car2 = prototype.clone('skylark', color='bmw')
print(car2)
