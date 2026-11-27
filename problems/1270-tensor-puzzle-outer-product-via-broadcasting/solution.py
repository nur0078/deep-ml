import numpy as np

def outer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Outer product of 1-D arrays a and b via broadcasting."""
    # Your code here
    res = [[] for _ in range(len(a))]
    for i in range(len(a)):
        for j in b:
            res[i].append(a[i] * j)
    return res
