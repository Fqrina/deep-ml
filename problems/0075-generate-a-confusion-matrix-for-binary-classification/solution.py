
from collections import Counter

def confusion_matrix(data):
    tp=0
    fp=0
    tn=0
    fn=0
    for inside in data:
        if inside[0] == 1 and inside[1] ==1:
            tp+=1
        elif inside[0] == 0 and inside[1] ==1:
            fp+=1
        elif inside[0] == 1 and inside[1] ==0:
            fn+=1
        elif inside[0] == 0 and inside[1] ==0:
            tn+=1
    return [[tp, fn], [fp,tn]]