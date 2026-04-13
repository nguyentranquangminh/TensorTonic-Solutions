def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    intersection_x = 0
    intersection_y = 0
    
    if box_a[0] > box_b[0]:
        swap(box_a, box_b)
    intersection_x = max(0, min(box_a[2], box_b[2]) - max(box_a[0], box_b[0]))

    if box_a[1] > box_b[1]:
        swap(box_a, box_b)
    
    intersection_y = max(0, min(box_a[3], box_b[3]) - max(box_a[1], box_b[1]))
    # print(intersection_x, intersection_y)
    intersection_area = intersection_x * intersection_y
    union_area = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1]) + (box_b[2] - box_b[0]) * (box_b[3] - box_b[1]) - intersection_area
    return intersection_area / union_area
    pass