def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    bin = [0]*256
    
    for i in image:
        for j in i:
            bin[j] += 1
    return bin