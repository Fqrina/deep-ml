import numpy as np
def softplus(x: float) -> float:
	"""
	Compute the softplus activation function.

	Args:
		x: Input value

	Returns:
		The softplus value: log(1 + e^x)
	"""
	return np.log(1+np.exp(x))