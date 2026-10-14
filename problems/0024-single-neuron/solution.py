import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	def sigmoid(z):
		return 1/(1+np.exp(-z))
	labels = np.array(labels)
	probabilities = [np.array(arr) @ np.array(weights) for arr in features]
	probabilities = np.array(probabilities) + bias
	probabilities = sigmoid(probabilities)
	mse = np.mean((labels-probabilities)**2)
	
	return np.round(probabilities, decimals=4).tolist(), np.round(mse, decimals=4)