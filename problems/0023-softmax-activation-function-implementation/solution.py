import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    scores_arr = np.array(scores)
    xp = np.exp(scores_arr - np.max(scores_arr))
    return (xp / np.sum(xp)).tolist()