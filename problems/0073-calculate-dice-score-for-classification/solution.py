
import numpy as np

def dice_score(y_true, y_pred):
    tp=0
    tn=0
    fp=0
    fn=0
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            tp+=1
        elif y_true[i] == 0 and y_pred[i] == 1:
            fp+=1
        elif y_true[i] == 1 and y_pred[i] == 0:
            fn+=1
        elif y_true[i] == 0 and y_pred[i] == 0:
            tn+=1
    if 2*tp+fp+fn==0:
        return 0
    res = (2*tp)/(2*tp+fp+fn)
    return round(res, 3)
