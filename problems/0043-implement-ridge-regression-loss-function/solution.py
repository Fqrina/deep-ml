import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	xprd = X @ W
	left = np.mean((y_true-xprd)**2)
	right = np.sum(w**2) * alpha
	return left+right