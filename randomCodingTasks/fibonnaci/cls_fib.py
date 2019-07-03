

class Fib:

    def __init__(self, element):
        self.element = element


    def __iter__(self):
        self.x, self.y = 0, 1

    def __next__(self):
        fib = self.x
        if fib > self.element:
            raise StopIteration
        self.x, self.y = self.y, self.y + self.x
        return fib


if __name__ == '__main__':

    fib = Fib(8)
    print(fib.__dict__)

    for f in Fib(8):
        print(f)
