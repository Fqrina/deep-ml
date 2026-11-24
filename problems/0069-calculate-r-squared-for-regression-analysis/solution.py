
import numpy as np

def r_squared(y_true, y_pred):
    mean = np.mean(y_true)
    sst = np.sum((y_true - mean)**2)
    ssr= np.sum((y_true - y_pred)**2)
    return 1-(ssr/sst)
