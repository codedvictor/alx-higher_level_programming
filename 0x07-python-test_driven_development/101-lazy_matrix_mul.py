#!/usr/bin/python3

"""2 matrices using numpy library"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 matrices
    Returns: the product of the 2 matrices
    """

    return np.matmul(m_a, m_b)
