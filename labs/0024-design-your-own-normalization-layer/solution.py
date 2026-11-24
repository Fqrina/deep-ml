# --- cell 1 ---
import numpy as np

def normalize(x, eps=1e-8):
    rms = np.sqrt(np.mean(np.square(x), axis=-1, keepdims=True) + eps)
    return (x / rms) * 4.5

# --- cell 2 ---
