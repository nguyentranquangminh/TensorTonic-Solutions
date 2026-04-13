import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    y_true = np.array(y_true)
    y_score = np.array(y_score)
    sum = 0
    for y, z in zip(y_true, y_score):
        sum += np.maximum(0, margin - y * z)
    if reduction == "mean":
        return float(sum / len(y_score))
    else: return sum
    pass