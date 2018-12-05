def bottom():

    # Returning the yield lets the value that goes up the call stack to come right back
    # down.
    return (yield 42)

def middle():
    return (yield from bottom())

def top():
    return (yield from middle())

if __name__ == '__main__':
    gen = top()
    value = next(gen)
    print(value)

    try:
        value = gen.send(value * 2)
    except StopIteration as exc:
        value = exc.value
    print(value)