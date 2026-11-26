# --- cell 1 ---
import numpy as np

class MyReducer:
    """
    Implement your own dimensionality reduction to 10 dimensions.
    
    Your goal: Project high-dimensional data to 10 dimensions while
    preserving structure for classification.
    
    A k-NN classifier will be trained on your reduced data to evaluate quality.
    """
    
    def __init__(self):
        self.n_components = 10
        self.top_eigenvectors = 0
        # Add any attributes you need to store learned parameters
    
    def fit(self, X):
        """
        Learn the reduction from training data.
        
        Args:
            X: Training data, shape (n_samples, n_features)
        
        Returns:
            self
        """
        std = np.std(X, axis=0)
        std_safe = np.where(std == 0, 1.0, std)
        normalized = (X - np.mean(X, axis=0))/std_safe
        cov = np.cov(normalized, rowvar=False)
        eigenvalues, eigenvectors = np.linalg.eigh(cov)
        sorted_idx = np.argsort(eigenvalues)[::-1]
        self.top_eigenvectors = eigenvectors[:, sorted_idx[:self.n_components]]
    
        for i in range(self.top_eigenvectors.shape[1]):
            vec = self.top_eigenvectors[:, i]
            non_zero = np.flatnonzero(~np.isclose(vec, 0.0, atol=1e-8))
            if len(non_zero) > 0 and vec[non_zero[0]] < 0:
                self.top_eigenvectors[:, i] = -vec
        return self
    
    def transform(self, X):
        """
        Apply the learned reduction to data.
        
        Args:
            X: Data to transform, shape (n_samples, n_features)
        
        Returns:
            X_reduced: shape (n_samples, 10)
        """
        return X @ self.top_eigenvectors
    
    def fit_transform(self, X):
        """Fit and transform in one step."""
        return self.fit(X).transform(X)