import numpy as np

def triu_ones(n: int) -> np.ndarray:
    """n x n upper-triangular matrix of ones (including diagonal)."""
    # Your code here
    res = [[] for _ in range(n)] 

    for i in range(n):
        for j in range(n):
            if i <= j:
                res[i].append(1.0)
            else:
                res[i].append(0.0)

    return res
