import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
    h1 = np.maximum(w1@x, 0)
    h2 = w2 @ h1
    return np.maximum(h2+x, 0)