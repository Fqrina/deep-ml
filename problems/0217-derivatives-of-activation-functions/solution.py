import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	d = {}
	sig = 1/(1+np.exp(-x))
	dersig = sig * (1 - sig)
	tanh = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
	dertanh = 1- tanh**2
	if x > 0:
		derrel = 1
	else:
		derrel = 0
	d["sigmoid"] = dersig
	d["tanh"] = dertanh
	d["relu"] = derrel
	return d