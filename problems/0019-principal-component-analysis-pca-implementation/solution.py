import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    std = np.std(data, axis=0)
    std_safe = np.where(std == 0, 1.0, std)
    normalized = (data - np.mean(data, axis=0))/std_safe
    cov = np.cov(normalized, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    sorted_idx = np.argsort(eigenvalues)[::-1]
    top_eigenvectors = eigenvectors[:, sorted_idx[:k]]

    for i in range(top_eigenvectors.shape[1]):
        vec = top_eigenvectors[:, i]
        non_zero = np.flatnonzero(~np.isclose(vec, 0.0, atol=1e-8))
        if len(non_zero) > 0 and vec[non_zero[0]] < 0:
            top_eigenvectors[:, i] = -vec
    return np.round(top_eigenvectors, 4)
    
