import numpy as np

def vstack(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Stack 1-D arrays a and b as rows of a (2, n) matrix."""
    # Your code here
    
    # Two vectors
    res = [a.tolist(), b.tolist()]
    return res


# ANY NUM OF VECTORS

# def vstack(*arrays: np.ndarray) -> np.ndarray:
    # res = []
    # for arr in arrays:
    #     res.append(arr.tolist())

    # return np.array(res)