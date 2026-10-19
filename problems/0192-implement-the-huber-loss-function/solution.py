import numpy as np
def huber_loss(y_true, y_pred, delta=1.0):
	"""
	Compute the Huber Loss between true and predicted values.

	Args:
		y_true (float | list[float]): Ground truth values
		y_pred (float | list[float]): Predicted values
		delta (float): Transition threshold between MSE and MAE behavior

	Returns:
		float: Average Huber loss
	"""
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)
	absloss = np.sum(np.abs(y_true - y_pred))
	mask = np.where(np.abs(y_true-y_pred) <= delta, 1, 0)
	loss = []
	try:
		for i in range(len(mask)):
			if mask[i] == 1:
				loss.append(0.5 * (y_true[i] - y_pred[i])**2)
			else:
				loss.append(delta * abs(y_true[i] - y_pred[i]) - 0.5 * delta**2)
		return np.mean(loss)
	except:
		absloss = abs(y_true - y_pred)
		if absloss <= delta:
			return 0.5 * absloss**2
		else:
			return delta * absloss - 0.5 * delta**2
