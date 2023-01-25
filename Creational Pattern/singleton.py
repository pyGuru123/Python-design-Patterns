class Borg:
	"""The Borg design pattern"""

	_shared_data = {} # Attribute dictionary

	def __init__(self):
		# All the objects of the borg will share
		# the same dict thus making it act like a 
		# global variable.
		self.__dict__ = self._shared_data


class Singleton(Borg):
	"""The Singleton design pattern"""

	def __init__(self, **kwargs):
		super(Borg, self).__init__()
		self._shared_data.update(kwargs)

	def __str__(self):
		return str(self._shared_data)

s1 = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(s1)
s2 = Singleton(SMTP = "Simple Mail Transfer Protocol")
print(s2)

# Here the Borg dict is shared between the two objects of the singleton, basically it acts as a global variable for all objects of the singleton.