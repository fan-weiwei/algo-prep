import random

def consumer():
    while True:
        val = yield
        print(val)

def producer(c):
    c.send(None)
    while True:
        val = random.randint(1, 10)
        c.send(val)
        yield

if __name__ == '__main__':
    c = consumer()
    #c.send(None)
    p = producer(c)

    for i in range(10):
        next(p)