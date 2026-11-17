import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = 0.0
    y = 0.0
    z = 0.0
    for _ in range(n):
        xt = (b[0] - (A[0][1]*y+ A[0][2]*z))/A[0][0]
        yt = (b[1] - (A[1][0]*x+ A[1][2]*z))/A[1][1]
        zt = (b[2] - (A[2][0]*x+ A[2][1]*y))/A[2][2]
        x = xt
        y = yt
        z = zt 
    return [x, y, z]