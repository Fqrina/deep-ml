import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	tp = 0
	fp = 0
	fn = 0
	for i in range(len(y_true)):
		if y_true[i] == 1 and y_pred[i] == 1:
			tp+=1
		elif y_true[i] == 0 and y_pred[i] == 1:
			fp+=1
		elif y_true[i] == 1 and y_pred[i] == 0:
			fn+=1
	if tp+fp == 0:
		precision =0
	else:
		precision = tp/(tp+fp)
	if tp+fn == 0:
		recall = 0
	else:
		recall = tp/(tp+fn)
	return round((1+beta**2)* (precision*recall) / ((beta**2 * precision)+ recall), 3)
