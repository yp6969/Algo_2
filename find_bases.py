import numpy as np

def isBase(A):
    """
    determin if A is a base of subspace

    Parameters
    ----------
    A : np.array - matrix nXn

    Returns bool - True if the determinant is not 0
    """
    return np.linlang.det(A) != 0