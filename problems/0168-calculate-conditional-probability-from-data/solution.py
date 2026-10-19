def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    con = 0
    total = 0
    for i in range(len(data)):
      if data[i][0] == x:
        total+=1
      if data[i][1] == y and data[i][0] == x:
        con+=1
    try:
      return float(con/total)
    except:
      return 0