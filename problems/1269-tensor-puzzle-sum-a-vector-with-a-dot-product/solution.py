import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    # Your code here
    res = 0
    for i in a: res+= i
    return res
