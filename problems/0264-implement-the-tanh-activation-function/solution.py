import math

def tanh(x: float) -> float:
    """
    Implements the Tanh (hyperbolic tangent) activation function.

    Args:
        x (float): Input value

    Returns:
        float: The tanh of the input, rounded to 4 decimal places
    """
    e1= math.exp(x)
    e2 = math.exp(-x)
    return (e1-e2)/(e1+e2)