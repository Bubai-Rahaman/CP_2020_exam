"""
SVD of a matrix
"""
import numpy as np

#1st matrix
A = np.array(((2, 1), (1, 0), (0, 1)))

U1, S1, VT1 = np.linalg.svd(A)

print("Singular values of the 1st matrix are", S1)

#2nd matrix
B = np.array(((1, 1, 0), (1, 0, 1), (0, 1, 1)))

U2, S2, VT2 = np.linalg.svd(B)

print("and singular values of the 2nd matrix are", S2)
