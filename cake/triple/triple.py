list_of_ints = [-10, -10, 1, 3, -100]

def max_product(arr):
    s = sorted(arr)
    option_one = s[0] * s[1] * s[-1]
    option_two = s[-3] * s[-2] * s[1]

    return max(option_one, option_two)

print(max_product(list_of_ints))