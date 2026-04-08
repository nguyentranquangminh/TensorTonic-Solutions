import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if (len(y) == 0):
        return float(0)
    values, counts = np.unique(y, return_counts=True)
    res = 0
    for c in counts:
        res -= (c / len(y)) * np.log2(c / len(y))
    return res