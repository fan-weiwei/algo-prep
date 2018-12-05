"""
Exploration of yield and consumers
"""

def simpleGenerator():
    yield 1
    yield 2
    yield 3


def nextSquare(n):
    i = 1

    while i < n:
        yield i ** 2
        i += 1

class PowTwo:

    __slots__ = ['n', 'max']

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            pow = 2 ** self.n
            self.n += 1
            return pow
        else:
            raise StopIteration()

if __name__ == '__main__':

    '''
    for i in simpleGenerator():
        print(i)
    '''

    arr_1 = [2 ** x for x in range(3)]
    print(type(arr_1))


    iter_1= iter(arr_1)
    print(next(iter_1))
    print(iter_1.__next__())
    print(next(iter_1))
    print('******')

    ## custom iterator
    iter_2 = PowTwo(4)
    for i in iter_2:
        print(i)
    print('******')

    ### iter has two arguments
    iter_3 = iter(int, 1)
    print(next(iter_3))

    print('******')

    ### generator syntax
    iter_3 = (2 ** x for x in range(3))
    for x in iter_3:
        print(x)

    print('******')

    ### generator syntax
    for x in (2 ** x for x in range(3)):
        print(x)
    else:
        print('done')
    print('******')


    print(* ([2 ** x] * 2 for x in range(3)))