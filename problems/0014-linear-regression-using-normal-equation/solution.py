import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X = np.array(X)
	y = np.array(y)
	
	first = np.linalg.inv(X.T @ X)
	sec = X.T @ y

	theta = first @ sec

	return theta