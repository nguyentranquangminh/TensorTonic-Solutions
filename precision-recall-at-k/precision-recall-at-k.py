def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    recommended_k = recommended[:k]
    common = list(set(recommended_k) & set(relevant))
    precision = len(common)/k
    recall = len(common)/len(relevant)
    return [precision, recall]