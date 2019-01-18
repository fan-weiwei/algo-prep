HIGHEST_POSSIBLE_SCORE = 100

def super_sort(arr):
    slots = []
    for index in range(HIGHEST_POSSIBLE_SCORE + 1):
        slots.append([])

    for item in arr:
        slots[item] += [item]

    result = []
    for slot in slots:
        for item in slot:
            result += [item]

    return result


if __name__ == '__main__':
    arr = [4, 5, 1, 2, 99, 99]
    print(super_sort(arr))
    print('here')