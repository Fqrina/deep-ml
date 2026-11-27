import numpy as np

def train_logreg(X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int) -> tuple[list[float], ...]:
    """
    Gradient-descent training algorithm for logistic regression, optimizing parameters with Binary Cross Entropy loss.
    """
    lossarray = []
    n_samples, n_features = X.shape
    theta = np.zeros((n_features+1)) 
    X_b = np.column_stack([np.ones((n_samples, 1)), X])  #n_samples, n_features+1
    for _ in range(iterations):
        h1 = X_b @ theta
        y_pred = 1/(1+np.exp(-np.clip(h1, -500,500)))
        loss = - np.sum(y * np.log(y_pred) + (1-y) * np.log(1-y_pred))
        theta -= learning_rate * X_b.T @ (y_pred - y)
        lossarray.append(loss)
    return (theta.tolist(), lossarray)
