import numpy as np
def precision(y_true, y_pred):
	tp = 0
	fp = 0
	for i in range(len(y_true)):
		if y_true[i] == 1 and y_true[i] == y_pred[i]:
			tp +=1
		elif y_pred[i] == 1 and y_true[i] == 0:
			fp+=1
	if tp+fp==0:
		return 0.0
	return tp/(tp+fp)
