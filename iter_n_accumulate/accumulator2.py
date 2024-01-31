"""
CS210 W24
This session covers
    - Iterables
    - Accumulator Pattern
    - Higher order functions
Author: Jose Renteria

"""
# What is an iterable?
    # an object that can be iterated over
    # i.e. lists, strings, tuples, sets, dicts, or iter object

# Slight difference between an iterable and an iterator
    # an iterator is an object that represents a STREAM of data.
    #  it is an object that represents a specific
    #  iteration (step-by-step process) over an iterable. It keeps 
    #  track of the current position in the iterable and provides the next item when requested.

# Example
# Is this an iterator or an iterable?
cards = ['Ace', 'Jack', 'Queen', 'King']

# Is this an iterator or an iterable?
dealer = iter(cards)
print((dealer, cards))

# <list_iterator object at 0x7f2c6c5b0760> vs ['Ace', 'Jack', 'Queen', 'King']
# Not human readable, and not meant to be. Meant for operations by the machine.
deal1 = next(dealer)
deal2 = next(dealer)
print(deal1, deal2)

# what is a function?
#   a block of reusable code that performs a specific task. 
#   Functions can take input values (arguments), process them, and return a result.

# What is a higher order function?
#   A higher-order function is a function that either takes one or more functions as 
#   arguments or returns a function as its result. In other words, it treats functions as 
#   first-class citizens, allowing them to be used as values.

# Activity:
#   We will write the reduce function in python, which is a higher order functions
#   Apply function of two arguments cumulatively to the items of iterable, 
#   from left to right, so as to reduce the iterable to a single value.
#   Does this seem familiar? What technique/pattern can we use here?

def reduce(function, iterable, initial_value=None):
    """
    Apply a binary function cumulatively to the items of an iterable, from left to right.

    Args:
        f (callable): A binary function that takes two arguments and returns a single result.
        iterable (iterable): An iterable (e.g., a list, tuple) whose elements will be reduced.
        initial_value (optional): An optional initial value for the accumulator. If not provided, the first element
            of the iterable will be used. Defaults to None.

    Returns:
        The result of the reduction.
    """
    pass # Remove this before you begin
    # initialize an iterator variable and pass in your iterable 
    # check if your initial value is empty:
    #   then you want to move it to the next item in your iterator
    # else:
    #   assign your accumulator variable to your initial value
    # for every element in your iterator:
    #   accumulate to your accumulator variable by calling the function 
    #   with the element passed into the function 
    # return your accumulated variable

# Some helper functions so we can pass into our reduce function
def add_nums(x: int, y: int):
    return x + y

def sub_nums(x: int, y:int):
    return x - y

def floor_nums_add(x: int, y: int):
    return x // 2 + y // 2

if __name__ == '__main__':
    nums = [1,2,3]
    print(reduce(add_nums, nums, 0))
    print(reduce(sub_nums, nums, 0))
    print(reduce(floor_nums_add, nums, 0))