import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    mse_values = []
    n_samples = len(features)
    for _ in range(epochs):
        d1 = np.dot(features, initial_weights) + initial_bias
        predict = 1/(1+np.exp(-d1))
        loss = predict-labels
        mse_values.append(float(np.mean(loss**2)))
        sigl = predict * (1-predict)
        d_loss_dz = (2 / n_samples) * loss * predict * (1 - predict)
        dw = np.dot(features.T, d_loss_dz)
        db = np.sum(d_loss_dz)
        initial_bias -= learning_rate*db
        initial_weights -= learning_rate*dw
    updated_weights = initial_weights
    updated_bias = initial_bias
    return updated_weights, updated_bias, mse_values