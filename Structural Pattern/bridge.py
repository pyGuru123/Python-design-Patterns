class DrawingAPIOne:
	"""Implementation-specific abstraction : concrete class 1"""
	def draw_circle(self, x, y, radius):
		print("API 1 drawing a curcle at ({}, {}) with radius {}".format(x, y, radius))


class DrawingAPITwo:
	"""Implementation-specific abstraction : concrete class 2"""
	def draw_circle(self, x, y, radius):
		print("API 2 drawing a curcle at ({}, {}) with radius {}".format(x, y, radius))


class Circle:
	"""Implementation-independent abstraction"""

	def __init__(self, x, y, radius, drawing_api):
		"""Initialize the necessary attributes"""
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	def draw(self):
		"""Implementation specific absratction taken crae of by another"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent):
		"""Implementation-independent"""
		self._radius *= percent

# *********************************************************

circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()

circle2 = Circle(1, 2, 3, DrawingAPITwo())
circle2.draw()