import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    n = len(A)
    res = 0
    for i in range(n):
        res += A[i][i]
    return res    
    pass
