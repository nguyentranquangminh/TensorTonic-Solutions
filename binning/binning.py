
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    v_max = max(values)
    v_min = min(values)
    if v_min == v_max:
        return [0] * len(values)
    width = (v_max - v_min) / num_bins
    res = []
    for v in values:
        res.append(min((v - v_min) // width, num_bins - 1))
    return res