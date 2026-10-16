import numpy as np
from typing import List, Tuple
def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    rng = np.random.default_rng()
    ls = np.arange(n_samples)
    if shuffle==True:
        np.random.shuffle(ls)
    indic = n_samples // k
    remainder = n_samples % k
    length = np.full(k,indic)
    length[:remainder]+=1

    ret = []
    accsum = 0
    for i in range(k):
        val = ls[accsum:accsum+length[i]]
        train = np.hstack([ls[:accsum], ls[accsum+length[i]:]])
        ret.append((train.tolist(), val.tolist()))
        accsum+=length[i]
    return ret

    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    pass