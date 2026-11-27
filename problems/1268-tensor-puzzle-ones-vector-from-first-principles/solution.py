import numpy as np

def ones(n: int) -> np.ndarray:
    """Return a length-n float vector of ones without calling np.ones."""
    # Your code here
    res = []
    for i in range(n):
        res.append(1)
    
    return res
