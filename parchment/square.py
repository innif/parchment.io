class Square:
	"""Implements basic functionality of squares on the grid.
	Squares have a state (empty, filled, connection or player) and can be assigned a colour. Each is accessed via setter and getter."""

	def __init__(self):
		self.state = "empty"

	def set_state(self, state):
		self.state = state

	def get_state(self):
		return self.state

	def set_colour(self, colour):
		self.colour = colour

	def get_colour(self):
		return self.colour