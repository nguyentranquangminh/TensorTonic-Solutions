import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    residual = np.array(np.array(y_true) - np.array(y_pred))
    lower = np.sum((1/2)*(residual[np.where(np.abs(residual) <= delta)]**2))
    higher = np.sum(delta * (np.abs(residual[np.where(np.abs(residual) > delta)]) - (1/2)*delta))
    return (higher + lower) / len(y_true)
    pass