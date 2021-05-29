import numpy as np

class ReLU:
	def __init__(self):
		self.mask = None

	def forward(self, x):
		self.mask = (x <= 0)
		out = x.copy()
		out[self.mask] = 0

		return out
	
	def backward(self, dout):
		dout[self.mask] = 0
		dx = dout

		return dx

class sidmoid:
	def __init__(self):
		self.out = None

	def forward(self, x):
		out = 1 / (1 + np.exp(-x))
		self.out = out

		return out

	def backward(self, dout):
		dx = dout * (1.0 - self.out) * self.out

		return dx

class SoftmaxWithLoss:
	def __init__(self):
		self.loss = None
		self.y = None # softmax 출력
		self.t = None # 정답 레이블

	def forward(self, x, t):
		self.t = t
		self.y = softmax(x)
		self.loss = cross_entropy_error(self.y, self.t)

		return self.loss

	def backward(self, dout=1):
		batch_size = self.t.shape[0]
		dx = (self.y - self.t) / batch_size

		return dx

if __name__ == '__main__':
	# check mask of relu
	x = np.array([[1.0, -0.5], [-2.0, 3.0]])
	print(x)

	mask = (x <= 0)
	print(mask)
