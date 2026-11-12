import numpy as np

def divide_on_feature(X, feature_i, threshold):
    idx = X[:, feature_i] >= threshold
    notidx= X[:, feature_i] < threshold
    fullfilled= X[idx]
    unfullfilled=X[notidx]
    return [fullfilled, unfullfilled] 