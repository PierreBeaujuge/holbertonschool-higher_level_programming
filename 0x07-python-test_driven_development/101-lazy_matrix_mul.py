#!/usr/bin/python3
"""
Module that handles
the multiplication of
two matrices using NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices using NumPy
    """
    return numpy.dot(m_a, m_b)
