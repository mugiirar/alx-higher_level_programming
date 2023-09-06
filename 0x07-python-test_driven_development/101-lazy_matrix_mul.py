#!/usr/bin/python3
import numpy as np
"""
matrix
"""


def lazy_matrix_mul(m_a, m_b):
    """
    defination
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for item in m_a:
        if type(item) is not list:
            raise TypeError("m_a must be a list of lists")

    for item in m_b:
        if type(item) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) != 0:
        for item in m_a:
            if len(item) == 0:
                raise ValueError("m_a can't be empty")

    if len(m_b) != 0:
        for item in m_b:
            if len(item) == 0:
                raise ValueError("m_b can't be empty")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for item in m_a:
        for element in item:
            if type(element) is not int and type(element) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for item in m_b:
        for element in item:
            if type(element) is not int and type(element) is not float:
                raise TypeError("m_b should contain only integers or floats")

    widh = len(m_a[0])
    for item in m_a:
        if len(item) != widh:
            raise TypeError("each row of m_a must be of the same size")

    rec = len(m_b[0])
    for item in m_b:
        if len(item) != rec:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = np.dot(m_a, m_b)

    return result_matrix
