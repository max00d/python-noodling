import numpy as np
from memory_profiler import memory_usage

def fib_iter(n: int = 50) -> int:
    x, y = 0, 1
    for i in range(n):
        print(f'the {i + 1} element in the sequence is {x:,}')
        if i + 1 == n:
            return x
        x, y = y, x + y


def fib_gen(n: int) -> int:
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x + y


if __name__ == '__main__':
    pass
    #
    # rv = fib_iter(8)
    # print(rv)
    #
    # rv = fib_gen(8)
    # vals = [v for v in rv]
    # print(vals)
