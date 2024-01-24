"""
CS210 W24
Iterables & Accumulator pattern
Author: Jose Renteria

"""


# Iterables
def iter_str(s: str):
    for char in enumerate(s):  # enumerate will return an (index, value)    (0, 1)   tuple,
        print(char)  # useful to see which iteration falls on which index, can index into the tuple
        # print(char[0]) accesses the index
        # print(char[1]) accesses the value


iter_str("string")

print("+---------Now lets see lists-----------+\n")


def iter_list(l: list):
    for el in l:
        print(el)


print("Will print elements in order, delimited by a newline character \n")
ints = [1, 2, 3]
chars = ['x', 'u', 'v']

iter_list(ints)
iter_list(chars)

print("+---------Alternatively-----------+\n")


# alternatively, you can iterate through a range of size len(l),
# but then you'd have to index into that list with your iteration var

def iter_list_alt(l: list):
    for el in range(len(l)):
        print(el)  # accesses the indices
        # print(l[el]) # access the value using the index


iter_list_alt(ints)
iter_list_alt(chars)

print("+----------Accumulator Activity-----------+\n")

"""
Outline for accumulator pattern

i. Instantiating a variable
ii. Iterating over a set of data, or a range until you meet a condition
iii. Updating the initial variable in some manner through each iteration
        ie. +=, -=, /=, &=. |=, etc

Let's put it to the test
"""


def sum_to_num(n: int) -> int:
    """


    Sum every single number up to our input n
    Start at some sum 0
    (0 + 1) + 2 + 3 + 4 + 5 + 6
    (1 + 2) + 3 + 4 + 5 + 6, the calculation in the parenthesis happens first
    (3 + 3) + 4 + 5 +6
    (6 + 4) + 5 + 6
    (10 + 5) + 6
    (15 + 6)
    21
    Notice how tedious this is, we can use a loop to get it done faster
    """
    sum = 0
    for i in range(n + 1):  # include the last value
        sum += i  # update your sum variable with your iteration variable
    return sum


def equality_counter(values: list, check: int) -> int:
    """
    Determine how many values in our list are equal to a specified value
    """
    count = 0  # initialize counter
    for el in values:  # iterate through the values list directly
        if el == check:  # if the current iteration matche the value you're checking
            count += 1  # increment the counter
    return count


# Error Messages
"""

How to read them
How to fix them

"""


def read_element(iterable: list, i: int):
    element = iterable[i]
    return element
    # try element[i]


if __name__ == '__main__':
    print(sum_to_num(6))
    assert (sum_to_num(6) == 21)

    values = [1, 2, 3, 3, 3, 3, 4, 5]
    print(equality_counter(values, 3))
    assert (equality_counter(values, 3) == 4)

    print(read_element([1, 2, 3], 1))