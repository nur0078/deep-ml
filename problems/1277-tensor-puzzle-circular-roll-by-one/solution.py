import numpy as np

def roll(a: np.ndarray) -> np.ndarray:
    """Circular left shift by one."""
    # Your code here
    n = len(a)
    out = [0] * n
    for i in range(n):
        out[i] = a[(i + 1) % n]
    

    return out
