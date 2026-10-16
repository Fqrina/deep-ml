import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	scores = np.array(scores)
	mx = np.max(scores)
	rlog = np.log(np.sum(np.exp(scores-mx)))
	return scores-mx-rlog