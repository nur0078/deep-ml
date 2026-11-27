import numpy as np

def flatten(A: np.ndarray) -> np.ndarray:
    """Row-major flatten of 2-D array A without reshape/ravel."""
    # Your code here
    a = tuple(A)
    res = []

    for i in A:
        res += (i.tolist())

    return(res)
    
