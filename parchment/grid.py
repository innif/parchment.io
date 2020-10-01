class Grid:
	"""implements functions of a playing field for parchment.io"""
	def __init__(self, x, y):
		self.grid = []
		row = []
		for i in range(y):
			for j in range(x):
				row.append({"state": "empty"})
			self.grid.append(row)
			row = []