import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	x=np.array(x)
	if n_col == None:
		n_col = len(np.unique(x))
	mat = np.zeros((len(x), n_col), dtype=np.float64)
	mat[np.arange(len(x)), x] = 1.0
	return mat