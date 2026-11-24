import numpy as np


def gini_impurity(y):
    """
    Calculate Gini Impurity for a list of class labels.

    :param y: List of class labels
    :return: Gini Impurity rounded to three decimal places
    """
    if len(y) == 0:
        return 0.0

    arr = np.asarray(y)
    _, counts = np.unique(arr, return_counts=True)
    probs = counts / len(arr)

    # sum_sq = 0.0
    # for p in probs:
    #     sum_sq += p ** 2
    sum_sq = np.sum(probs**2)

    val = 1.0 - sum_sq
    return round(float(val), 3)