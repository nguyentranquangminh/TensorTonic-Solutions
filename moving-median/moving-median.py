def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    ans = []
    for i in range(window_size, len(values) + 1):
        arr = []
        for j in range(i - window_size, i):
            arr.append(values[j])
        arr.sort()
        if (window_size % 2 == 0):
            ans.append(abs(arr[window_size // 2 - 1] + arr[window_size // 2]) / 2)
        else: ans.append(abs(arr[window_size // 2]))
    return ans