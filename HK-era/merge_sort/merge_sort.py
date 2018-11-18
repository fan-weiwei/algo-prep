unsorted_array = [5, 6, 0, 1, 2, 7, 6, 5, 1, 10, 11, 12, 67, 2, 6, 9, 32]


def merge_sort(arr):
    if len(arr) <= 1: return arr

    pivot = arr[0]
    left = []
    right = []
    for element in arr[1:]:
        if element > pivot:
            right.append(element)
        if element <= pivot:
            left.append(element)

    return merge_sort(left) + [pivot] + merge_sort(right)

print(merge_sort(unsorted_array))