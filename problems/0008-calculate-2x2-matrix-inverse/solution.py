import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    # Your code here

    # (a, b), (c, d) = matrix
    m = np.array(matrix, dtype=float)
    
    if np.isclose(np.linalg.det(m), 0):
        return None
    return np.linalg.inv(m).tolist()
    