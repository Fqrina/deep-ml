
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    tp=0
    tn=0
    fp=0
    fn=0
    for i in range(len(actual)):
        if actual[i] == 1 and predicted[i] == 1:
            tp+=1
        elif actual[i] == 0 and predicted[i] == 1:
            fp+=1
        elif actual[i] == 1 and predicted[i] == 0:
            fn+=1
        elif actual[i] == 0 and predicted[i] == 0:
            tn+=1
    if tp+tn+fp+fn == 0:
        accuracy = 0
    else:
        accuracy = (tp+tn)/(tp+tn+fp+fn)
    if tp+fp == 0:
        f1_score = 0
    else:
        precision = tp/(tp+fp)
    if tp+fn == 0:
        f1_score = 0
    else:
        recall = tp/(tp+fn)
    f1_score = (2*precision*recall)/(precision+recall)
    if tn+fp == 0:
        specifity = 0
    else:
        specifity = tn/(tn+fp)
    if tn+fn == 0:
        npv=0
    else:
        npv = tn/(tn+fn)
    confusion_matrix = [[tp, fn], [fp, tn]]
    return confusion_matrix, round(accuracy, 3), round(f1_score, 3), round(specifity, 3), round(npv, 3)
