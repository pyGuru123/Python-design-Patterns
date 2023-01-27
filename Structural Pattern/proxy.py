import time

class Producer:
	"""Define the resource intensive object to instantiate!"""

	def produce(self):
		print("Producer is working hard")

	def meet(self):
		print("Producer has time to meet you now")

class Proxy:
	"""Define the relatively less resource intensive proxy as placeholder"""

	def __init__(self):
		self.occupied = 'No'
		self.producer = None

	def produce(self):
		"""Chcek if producer is available"""
		print("Artist checking if producer is available...")

		if self.occupied == 'No':
			# If the producer is available create a produce object
			self.producer = Producer()
			time.sleep(2)

			# Make the producer meet the guest
			self.producer.meet()

		else:
			# The producer is not available
			time.sleep(2)
			print('producer is busy!')

# Creating a proxy object
proxy = Proxy()
proxy.produce()
proxy.occupied = 'Yes'
proxy.produce()