"""
Author: Jose Renteria
For CS210 Class Encore

- Practice with list comprehensions

- Practice passing a function as an argument using Map
Also observing usage of Map

Map function takes a function and an iterable as input:

            Map(function*, iterable)

and returns an object that can be iterated over. (AKA an ITERABLE TYPE)

The function is applied to each element of the iterable, and the result is
returned as a new iterable containing the results.
"""

import unittest

# function that returns input x squared
def square(x):
    return x ** 2


squared = (map(square, range(1,5)))

# Notice how this is able to iterate over
# each element in 'squared' but when
# you print the object it is just a map object at a mem location

#for el in squared:
#    print(el)

# <map object at 0x000001D705F6FD90>
# Need to type cast to a list if you want it to print as a list
print(list(squared), "Map function")


# List comprehensions can allow us to quickly generate new lists
# A list comprehension iterates over each item in the iterable
# if a condition is provided, only items for which the condition
# is 'True' are included in the resulting new list
# For each item, the expression is evaluated, and the result is 
# appended to the new list
# 
#    The basic syntax for a list comprehension:
#
#        [(expression) for item in iterable if condition]
#            Note: (if-statement optional)
#
# Example:

squares = [(x ** 2) for x in range(1,5)]

print(squares, "List comprehension")

# This achieved the same functionality as mapping our square()
# Function to each item in our iterable range

# Tips:
# Start with simple comprehensions and gradually increase complexity.
# Keep them readable; avoid overly complex comprehensions.
# Use comprehensions where they enhance readability and maintainability


def vector_dilate(vector: list, scalar: int):
    """
    A vector dilation is a type of linear transformation that scales a vector
    by a scalar factor. Given a vector v in a vector space and a scalar s, the
    dilation of v by s is a new vector v' s.t. v' = s * v

    vector_dilate([1, 0, 0], 3)
    >>> [3, 0, 0]

    """
    # TODO
    # initialize a locally-scoped auxiliary scale function that
    # takes in an integer and multiplies it by the given scalar
    #
    # map this auxiliary function to every component in the given vector
    # and return it as a list
    #
    # you  want to apply your auxiliary scale function to everything in 
    # the vector using the map() function
    # we cast it to list so that it is readable


def vector_dilate_comp(vector: list, scalar: int):
    """
    We want to accomplish the same functionality as vector_dilate() but using
    a list comprehension. 

    Remember the syntax for a list comprehension
        [(expression) for item in iterable if condition]
            Note: (if-statement optional)
    """
    # TODO
    # First think about your expression
    # Then think about how you can use that to 
    # scale every component in the vector
    # and return it as a list

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