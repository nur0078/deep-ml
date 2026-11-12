import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    w = np.array(weights, dtype=float)   # copy so the input isn't modified
    n_samples = X.shape[0]

    for i in range(n_iter):
        j = i % n_samples                # cycle through samples in order, no shuffling
        x_i, y_i = X[j], y[j]

        pred = x_i @ w                   # scalar: x_i · w
        grad = 2 * (pred - y_i) * x_i    # (n_features,): per-sample MSE gradient
        w -= learning_rate * grad        # gradient descent step

    return w.tolist()

    #DIY