import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    """

    X_b = X[batch_indices]      # (m, D)
    y_b = y[batch_indices]      # (m,)

    m = len(batch_indices)
    
    y_pred = X_b @ weights + bias               # (m,)
    errors = y_pred - y_b                       # (m,)

    grad_w = (2 / m) * (X_b.T @ errors)         # (D,)
    grad_b = (2 / m) * errors.sum()             # scalar

    new_w = weights - lr * grad_w
    new_b = bias - lr * grad_b

    return np.concatenate([new_w, [new_b]])     # (D+1,)