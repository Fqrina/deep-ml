import numpy as np
def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	tp = 0
	fp = 0
	fn = 0
	for i in range(len(y_true)):
		if y_pred[i] == 1 and y_true[i] == 1:
			tp +=1
		elif y_pred[i] == 0 and y_true[i] == 1:
			fn +=1
		elif y_pred[i] == 1 and y_true[i] == 0:
			fp +=1
	if tp + fp == 0 or tp + fn == 0:
		return 0
	precision = tp/(tp+fp)
	recall=tp/(tp+fn)
	return round(2 * (precision * recall) / (precision + recall), 3)