class Korean:
	"""Korean Speaker"""
	def __init__(self):
		self.name = "korean"

	def speak_korean(self):
		return "An-neyong!"

class British:
	"""English Speaker"""
	def __init__(self):
		self.name = "British"

	def speak_english(self):
		return "Hello!"


class Adapter:
	"""This changes the generic method name to individualized method names"""
	def __init__(self, object, **adapted_method):
		self._object = object

		# Add a new dictionary which eastablishes the mapping between
		# generic method and individual methods.
		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		"""Simply returns the rest of the attributes"""
		return getattr(self._object, attr)


# List to store speaker objects
objects = []

# Korean Speaker Object
korean = Korean()

# English Speaker Object
british = British()

# Append the objects to objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
	print("{} says {}".format(obj.name, obj.speak()))