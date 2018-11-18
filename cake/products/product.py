arr = [1, 7, 3, 4, 0]

def weird_product2(arr):

    previous = 1
    partial = []

    for v in arr:
        partial.append(previous)
        previous *= v

    previous = 1
    result = []

    for v, part in zip(reversed(arr), reversed(partial)):
        result.append(part * previous)
        previous *= v

    return list(reversed(result))


def weird_product(arr):

    previous = 1
    result = []

    for v in arr:

        result = [r * v for r in result]
        result.append(previous)
        previous *= v

    return result


print(weird_product2(arr))

