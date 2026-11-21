import numpy as np

def square_relu(x: np.ndarray) -> dict:
    """
    Apply the Square ReLU activation function and compute its derivative.
    
    Args:
        x: Input numpy array of any shape
    
    Returns:
        Dictionary with 'output' and 'derivative' as numpy arrays
    """
    res = np.where(x > 0, x**2, 0)
    der = np.where(x > 0, 2*x, 0)
    return {"output": res, "derivative":der}