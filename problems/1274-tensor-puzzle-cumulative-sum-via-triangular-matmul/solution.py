import numpy as np

def cumsum(a: np.ndarray) -> np.ndarray:
    """Inclusive cumulative sum of 1-D array a without np.cumsum."""
    count = 0
    res = []
    # Your code here
    for i in a:
        count += i
        res.append(count)

    return res
