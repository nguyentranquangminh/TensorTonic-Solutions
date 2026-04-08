import numpy as np 
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    res = []
    for x0 in x:
        val = x0 if x0 >= 0 else alpha * (np.exp(x0) - 1)
        res.append(val)
    return res