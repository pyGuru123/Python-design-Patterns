class Component:
	"""Abstract class"""

	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		pass

class Child(Component):
	"""Concrete class"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		# This is where we are going to store the name of the child item
		self.name = args[0]

	def component_function(self):
		# Print the name of the child item here
		print('{}'.format(self.name))

class Composite(Component):
	"""Concrete class"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		# This is where we store name of the composite object
		self.name = args[0]

		# This is where we keep our child items
		self.children = []

	def append_child(self, child):
		"""Method to add a new child item"""
		self.children.append(child)

	def remove_child(self, child):
		"""Method to remove a child item"""
		self.children.remove(child)

	def component_function(self):
		# Print the name of the composite object
		print('{}'.format(self.name))

		# Iterate through the child objects and initiate their component
		for child in self.children:
			child.component_function()

# *******************************************************************

# Build a composite submenu 1
sub1 = Composite("submenu1")

# Create new child submenu 11
sub11 = Child("submenu 11")
# Create new child submenu 12
sub12 = Child("submenu 12")

# Add the submenu 11 to submenu 1
sub1.append_child(sub11)
# Add the submenu 12 to submenu 1
sub1.append_child(sub12)

# Build a top level composite menu
top = Composite("topmenu")

# build a submenu 2 that is not a composite
sub2 = Child("submenu 2")

# Add submenu 1 and submenu 2 to top menu
top.append_child(sub1)
top.append_child(sub2)

# Testing top menu
top.component_function()