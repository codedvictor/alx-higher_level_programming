 #!/usr/bin/python3
"""Defines a function  to multiply 2 matrices"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for x in m_a:
        if not isinstance(x, list):
            raise TypeError("m_a must be a list of lists")

    for x in m_b:
        if not isinstance(x, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for x in m_a:
        for i in x:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for x in m_b:
        for i in x:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    for x in m_a:
        if len(x) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for x in m_b:
        if len(x) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")

    mulvalue = [[sum(i * j for i, j in zip(x, y))
             for y in zip(*m_b)] for x in m_a]

    return (mulvalue)
