import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    x = np.asarray(x, dtype=float)
    analytical_grad = np.asarray(analytical_grad, dtype=float)

    num_grad = np.zeros_like(x)

    for i in range(x.size):
        step = np.zeros_like(x)
        step[i] = epsilon
        num_grad[i] = (f(x + step) - f(x - step)) / (2 * epsilon)

    numerator = np.linalg.norm(analytical_grad - num_grad)
    denominator = np.linalg.norm(analytical_grad) + np.linalg.norm(num_grad)
    relative_error = numerator / denominator if denominator > 0 else 0.0

    return num_grad, relative_error