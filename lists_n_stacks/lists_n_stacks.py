"""
Jose Renteria
For CS210 Class Encore W23

Practice with list operations and stacks

"""
# We have three auxiliary list functions
# We want to use them to write a higher order function
# that takes in an iterable and two functions and performs some
# operation on them

def pop(lst: str):
    return lst.pop()

def push(lst, x):
    return lst.append(x)

def remove(lst, x):
    return lst.remove(x)

def peek(lst, i):
    return lst[i]

def higher_order(lst: str, fn1, fn2):
    unique = []
    for char in lst:
        if char not in unique:
            fn1(unique, char)
        else:
            fn2(unique, char)
    return unique 

print(higher_order([1,2,2,4], push, remove))

