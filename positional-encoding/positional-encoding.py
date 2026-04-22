import numpy as np
import math

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    res = []
    for pos in range(seq_len):
        ans = []
        for i in range(d_model):
            if i % 2 == 0:
                ans.append(math.sin(pos / (base ** (i/d_model))))
            else: 
                ans.append(math.cos(pos / (base ** ((i-1)/d_model))))
        res.append(ans)
    return np.array(res)
    pass