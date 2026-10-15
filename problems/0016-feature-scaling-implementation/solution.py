import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	standardized_data = (data - np.mean(data, axis=0))/np.std(data, axis=0)
	mx = np.max(data, axis=0)
	mn = np.min(data, axis=0)
	normalized_data = (data-mn)/(mx-mn)
	return np.round(standardized_data, decimals=4).tolist(), np.round(normalized_data, decimals=4).tolist()