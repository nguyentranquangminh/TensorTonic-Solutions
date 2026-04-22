import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.array(X)

    if X.shape[0] == 1 or X.ndim != 2:
        return None 
    X = np.transpose(X)
    average = np.mean(X, axis = 1, keepdims = 1)
    X_centered = X - average
    return (X_centered @ X_centered.T) / (X.shape[1] - 1)
    pass








    