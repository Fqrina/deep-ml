import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    tp = 0
    fn = 0
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_true[i] == y_pred[i]:
            tp+=1
        else:
            if y_pred[i] == 0 and y_true[i] == 1:
                fn+=1
    if tp+fn == 0:
        return 0.0
    return tp/(tp+fn)