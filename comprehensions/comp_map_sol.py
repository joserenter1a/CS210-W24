"""
Author: Jose Renteria
For CS210 Class Encore

Solutions for the comprehension and map activity.
"""

import unittest

def vector_dilate(vector: list, scalar: int):
    """
    A vector dilation is a type of linear transformation that scales a vector
    by a scalar factor. Given a vector v in a vector space and a scalar s, the
    dilation of v by s is a new vector v' s.t. v' = s * v

    vector_dilate([1, 0, 0], 3)
    >>> [3, 0, 0]

    """
    def scale(x: int):
        return x * scalar
    return list(map(scale, vector))


def vector_dilate_comp(vector: list, scalar: int):
    """
    We want to accomplish the same functionality as vector_dilate() but using
    a list comprehension. 

    Remember the syntax for a list comprehension
        [(expression) for item in iterable if condition]
            Note: (if-statement optional)
    """
    return [(scalar * i) for i in vector]


class test_case(unittest.TestCase):
    def test_dilate_two(self):
        vector = [1, 2, 3]
        scalar = 2
        expected = [2, 4, 6]
        result = vector_dilate(vector, scalar)
        result2 = vector_dilate_comp(vector, scalar)
        self.assertEqual(result, expected)
        self.assertEqual(result2, expected)

    def test_dilate_zero(self):
        vector = [1, 2, 3]
        scalar = 0
        expected = [0, 0, 0]
        result = vector_dilate(vector, scalar)
        result2 = vector_dilate(vector, scalar)
        self.assertEqual(result, expected)
        self.assertEqual(result2, expected)

    def test_dilate_negative(self):
        vector = [1, 2, 3]
        scalar = -1
        expected = [-1, -2, -3]
        result = vector_dilate(vector, scalar)
        result2 = vector_dilate(vector, scalar)
        self.assertEqual(result, expected)
        self.assertEqual(result2, expected)

    def test_dilate_empty(self):
        vector = []
        scalar = 2
        expected = []
        result = vector_dilate(vector, scalar)
        result2 = vector_dilate(vector, scalar)
        self.assertEqual(result, expected)
        self.assertEqual(result2, expected)


if __name__ == '__main__':
    unittest.main()