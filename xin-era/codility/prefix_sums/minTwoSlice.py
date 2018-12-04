




def get_prefix_array(arr):

    prefix = [0]
    tally = 0
    for item in arr:
        tally += item
        prefix += [tally]

    return prefix

def average(prefix, left, right):
    return (prefix[right + 1] - prefix[left]) / (right - left + 1)


def solution(arr):

    prefix = get_prefix_array(arr)

    final_min = average(prefix, 0, 1)
    start_index = 0

    for left in range(len(arr) - 1):
        for right in range(left + 1 , min(len(arr), left + 3)):
            result = average(prefix, left, right)

            if result < final_min:
                start_index = left
                final_min = result

            final_min = min(final_min, result)


    return start_index





if __name__ == '__main__':
    example = [4,2,2,5,1,5,8]
    print(solution(example))