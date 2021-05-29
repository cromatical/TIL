import numpy as np

class Mullayer:
	def __init__(self):
		self.x = None
		self.y = None
	
	def forward(self, x, y):
		self.x = x
		self.y = y
		out = x * y
		
		return out

	def backward(self, dout):
		dx = dout * self.y
		dy = dout * self.x

		return dx, dy

class Addlayer:
	def __init__(self):
		pass

	def forward(self, x, y):
		out = x + y

		return out

	def backward(self, dout):
		dx = dout * 1
		dy = dout * 1

		return dx, dy

class Affine:
	def __init__(self, W, b):
		self.W = W
		self.b = b
		self.x = None
		self.y = None
		self.db = None
	
	def forward(self, x):
		self.x = x
		out = np.dot(x, self.W) + self.b

		return out

	def backward(self, dout):
		dx = np.dot(dout, self.W.T)
		self.dW = np.dot(self.x.T, dout)
		self.db = np.sum(dout, axis=0)

		return dx