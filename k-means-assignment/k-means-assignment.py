def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    ans = []
    for p in points:
        res = 0
        dist = 1e18 
        for i in range(len(centroids)):
            newDist = 0
            for j in range(len(p)):
                newDist += (p[j] - centroids[i][j])**2
            if dist > newDist:
                dist = newDist
                res = i
        ans.append(res)
    return ans