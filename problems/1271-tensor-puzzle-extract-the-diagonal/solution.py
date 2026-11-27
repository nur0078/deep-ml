import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    # Your code here
    res = []
    for i in range(len(A)):
        res.append(A[i][i])

    return res
