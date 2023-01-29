class Subject:
	"""Represents what is being observed."""

	def __init__(self):
		self._observers = []

	def attach(self, observer):
		# Append the observer to the observer list if not already there
		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):
		# Simply remove the observer
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

	def notify(self, modifier=None):
		# Notify all the observers when there's a change in the subject
		for observer in self._observers:
			if modifier != observer:
				observer.update(self)


class Core(Subject):
	def __init__(self, name=""):
		Subject.__init__(self)
		self._name = name
		self._temp = 0

	@property # Getter method to get the core temperature
	def temp(self):
		return self._temp

	@temp.setter # Setter method to set the core temperature
	def temp(self, temp):
		self._temp = temp 
		self.notify()

class TempViewver:
	def update(self, subject):
		# Alert method that is invoked when the temp changes
		print("Temperature Viewer : {} has temperature {}".format(subject._name, subject.temp))


# *********************************************************

# Creating subjects
c1 = Core('Core 1')
c2 = Core('Core 2')

# Creating Observers
v1 = TempViewver()
v2 = TempViewver()

# Attaching observers to first core
c1.attach(v1)
c1.attach(v2)

c1.temp = 80
c1.temp = 90