import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    ans = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(v[i])
            else: row.append(0)
        ans.append(row)
    return np.array(ans)
    pass
