import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""

	PARTIALS = {
		"poly2d": (lambda x, y: 2*x*y + y**2,      # ∂f/∂x
		           lambda x, y: x**2 + 2*x*y),     # ∂f/∂y
		"exp_sum": (lambda x, y: np.exp(x+y),      # ∂f/∂x
		            lambda x, y: np.exp(x+y)),     # ∂f/∂y
		"product_sin": (lambda x, y: np.sin(y),    # ∂f/∂x
		                lambda x, y: x*np.cos(y)), # ∂f/∂y
		"poly3d": (lambda x, y, z: 2*x*y,            # ∂f/∂x   TODO
		           lambda x, y, z: x**2 + z**2,            # ∂f/∂y   TODO
		           lambda x, y, z: 2*y*z),           # ∂f/∂z   TODO
		"squared_error": (lambda x, y: 2*x - 2*y,        # ∂f/∂x   TODO
		                  lambda x, y: 2*y - 2*x),       # ∂f/∂y   TODO
	}

	# TODO: look up PARTIALS[func_name], call each lambda on the point (use *point),
	res = tuple(d(*point) for d in PARTIALS[func_name])


	# and return the results as a tuple
	return res