import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	mat = []
	try:
		a = y[0]
		exist=True
	except:
		exist=False
	if exist:
		for loop in range(0,len(X), batch_size):
			data = X[loop:loop+batch_size]
			datay = y[loop:loop+batch_size]
			mat.append([data,datay])
	else:
		for loop in range(0, len(X), batch_size):
			data = X[loop:loop+batch_size]
			mat.append([data])
	return mat
	pass