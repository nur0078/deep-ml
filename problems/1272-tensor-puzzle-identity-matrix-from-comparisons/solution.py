import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""

    res = [[] for _ in range(n)] 
    # Your code here
    for i in range(n):
        for j in range(n):
            if i == j:
                res[i].append(1)
            else:
                res[i].append(0)

    return res
