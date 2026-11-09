import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	g = np.array(gradient, dtype=float)
	mag = np.linalg.norm(g)
		
	if mag == 0:
        direction = np.zeros_like(g)
    else:
        direction = g / mag

		
	

	return {
        'magnitude': float(mag),
        'direction': direction.tolist(),
        'descent_direction': (-direction).tolist(),
    }