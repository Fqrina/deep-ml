import math

def binomial_probability(n: int, k: int, p: float) -> float:
    return float(math.factorial(n)/(math.factorial(k)*(math.factorial(n-k))) * p**k * (1-p)**(n-k))
    """
    Calculate the probability of exactly k successes in n Bernoulli trials.
    
    Args:
        n: Total number of trials
        k: Number of successes
        p: Probability of success on each trial
    
    Returns:
        Probability of k successes
    """
    # Your code here
    pass