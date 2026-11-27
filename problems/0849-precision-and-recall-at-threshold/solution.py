import numpy as np

def precision_recall_at_threshold(y_true, y_scores, threshold):
    """
    Compute precision and recall at a given decision threshold.

    Args:
        y_true: list/array of true binary labels (0 or 1)
        y_scores: list/array of predicted scores in [0, 1]
        threshold: float, classification threshold (predict positive if score >= threshold)

    Returns:
        [precision, recall] as a list of two floats rounded to 4 decimals.
    """
    y_pred = np.where(np.array(y_scores) >= threshold, 1, 0)
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    # print(y_pred)
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            tp+=1
        elif y_true[i] == 1 and y_pred[i] == 0:
            fn+=1
        elif y_true[i] == 0 and y_pred[i] == 1:
            fp+=1
        else:
            tn+=1
    # print(tp, tn, fp, fn)
    precision = tp/(tp+fp) if tp+fp !=0 else 0
    recall = tp/(tp+fn) if tp+fn !=0 else 0
    return [round(precision, 4), round(recall, 4)]
