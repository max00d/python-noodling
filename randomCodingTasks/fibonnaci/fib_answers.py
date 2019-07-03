import functools

from time import time
from memory_profiler import memory_usage

@functools.lru_cache(maxsize=None)
def fib(n=50):
    if n < 0:
        return "GTFO"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    start = time()
    n = 50
    r = fib(n)
    print(f'result for {n}th element is: {r:,} took {time() - start:.2f} seconds')

    mem_usage = memory_usage(fib)
    print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print('Maximum memory usage: %s' % max(mem_usage))



