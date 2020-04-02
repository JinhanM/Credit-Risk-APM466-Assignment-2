import numpy as np
import scipy.linalg as alg
P = np.array([[0.8, 0.1, 0.1, 0], [0.1, 0.5, 0.2, 0.2], [0.1, 0.3, 0.3, 0.3],[0, 0, 0, 1]])
print(P)

# 1a
P_2yr = np.linalg.matrix_power(P, 2)
print(P_2yr)

# 1b
P_1month = alg.fractional_matrix_power(P, 1/12)
print(P_1month)

# 1c
P_1000yr = np.linalg.matrix_power(P, 1000)
print(P_1000yr)
