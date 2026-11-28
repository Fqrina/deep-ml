import numpy as np

def kmeans_plus_plus_init(X: np.ndarray, k: int, seed: int = None) -> np.ndarray:
    """
    Initialize k centroids using the K-Means++ algorithm.
    
    Args:
        X: Data points of shape (n_samples, n_features)
        k: Number of centroids to initialize
        seed: Random seed for reproducibility
    
    Returns:
        Centroids of shape (k, n_features)
    """
    np.random.seed(seed)
    idx = np.random.randint(len(X))
    centroid = np.array([X[idx]])
    dis = np.sum((centroid[:, None, :] - X[None, :, :])**2, axis=2) #centroid, X
    for i in range(k-1):
        realdis = np.min(dis, axis=0)
        probs = realdis / np.sum(realdis)
        idx = np.random.choice(len(X), p=probs)
        centroid = np.append(centroid, [X[idx]], axis=0)
        dis = np.sum((centroid[:, None, :] - X[None, :, :])**2, axis=2) #centroid, X 
    #initialize centroid done, next justloop
    return centroid