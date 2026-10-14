import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y = np.array(y)
	theta = np.linalg.pinv(X.T @ X) @ X.T @ y
	# Your code here, make sure to round
	return theta