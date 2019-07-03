# example 6 using a decorator and a function that takes arguments
def decorator_with_defined_args(func):
    def wrapper(arg1, arg2):
        print(f'the sum of {arg1} and {arg2}')
        func(arg1, arg2)
    return wrapper

@decorator_with_defined_args
def simple_add(x, y):
    print(f'equals {x + y}')

# simple_add = decorator_with_args(simple_add(5, 4))
simple_add(10, 5)

# example 7 decorator with many args
def decorator_with_unspecified_args(func):
    def wrapper(*args, **kwargs):
        print(f'args are {args}')
        print(f'key word args are {kwargs}')
        func(*args, *kwargs)
    return wrapper

@decorator_with_unspecified_args
def complex_add(x, y, a=0, b=0):
    print('testing')
    print(f'the sum of {x} + {y} + {a} + {b} = {int(x) + int(y) + int(a) + int(b)}')

complex_add(10, 20)
complex_add(5, 5, a=10, b=10)
