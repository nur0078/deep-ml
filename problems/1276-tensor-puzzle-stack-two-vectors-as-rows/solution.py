import numpy as np

def vstack(*arrays: np.ndarray) -> np.ndarray:
    """Stack 1-D arrays a and b as rows of a (2, n) matrix."""
    # Your code here
    
    # res = [a.tolist(), b.tolist()]
    res = []
    for arr in arrays:
        res.append(arr.tolist())

    return np.array(res)