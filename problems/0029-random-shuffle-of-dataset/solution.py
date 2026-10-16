import numpy as np

def shuffle_data(X, y, seed=None):
	if seed != None:
		np.random.seed(seed)
	idx = np.arange(len(X))
	np.random.shuffle(idx)
	X = X[idx]
	y = y[idx]
	return (X,y)
	# Your code here
	pass