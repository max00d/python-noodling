
# example one - just a function inside a function
def add_outer(n):
    def add_inner(n):
        return n + 1
    result = add_inner(n)
    return result

# example 2 - chain function calls
def plus_n(num, n):
    return num + n

def call_func(func):
    number = 10
    number_to_add = 5
    return func(number, number_to_add)

print(f'result of chain function call is: {call_func(plus_n)}')


# example 3 - nested functions - inner function has access to outer functions scope - called closure
def outer_func(s):
    def inner_func():
        print(f'outer_func argument is: {s}')
    inner_func()
outer_func('look at this!')

# example 4 - simple decorater convert string to camel case
def titlecase_decorator(func):
    def wrapper():
        f = func()
        make_titlecase = f.title()
        return make_titlecase
    return wrapper

def this_is_a_string():
    return 'i am a string'

decorate = titlecase_decorator(this_is_a_string)
print(f'result from the decorated function is: {decorate()}')

# >>> think about this - it is just accessing the inner function of titlecase_decorator
def wrapper():
    f = this_is_a_string()
    make_titlecase = f.title()
    return make_titlecase

print(f'this is the example of just calling the wrapper as a normal function: {wrapper()}')

#example 5 - use the function from example 4 as a decorator
@titlecase_decorator
def this_is_a_string():
    return 'i am a string'

print(f'decorated function result is: {this_is_a_string()}')
print(f'note that this is the same as calling > titlecase_decorator(this_is_a_string)(): '
      f'{titlecase_decorator(this_is_a_string)()}')

# example 6 - is a decorator not just a way of modifying a function?
from datetime import datetime
def cheeky_decorator(func):
    dt = datetime.now()
    def wrapper(x, y):
        print(f'the result should just be {x} + {y} = {x+y}')
        func(x, y + dt.day)
        print(f'but you got {x + y + dt.day} instead muhahaha!!')
    return wrapper

@cheeky_decorator
def just_add(x, y):
    print(f'the sum of {x} + {y} = {x + y}')

just_add(10, 20)






