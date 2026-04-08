import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    sum_probality = 0
    for v in p:
        sum_probality += v;
    if sum_probality != 1:
        raise(ValueError)
    res = 0
    for val1, val2 in zip(x, p):
        res += val1 * val2
    return res
    pass
