
def find_parent(i):
    if i == 0:
        return None
    return (i - 1) // 2

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2


def sift_up(heap, index, repeat=True):

    parent = find_parent(index)
    if parent:
        child_value = heap[index]
        parent_value = heap[parent]
        if child_value < parent_value:
            heap[index] = parent_value
            heap[parent] = child_value
            if repeat:
                sift_up(heap, parent)

def min_child(heap, index):
    l_index, r_index = left_child(index), right_child(index)
    if l_index >= len(heap):
        return None, None

    l_value = heap[l_index]
    if r_index >= len(heap):
        return l_index, l_value
    r_value = heap[r_index]

    if l_value < r_value:
        return l_index, l_value
    else:
        return r_index, r_value

def sift_down(heap, index, repeat=True):
    value = heap[index]
    child_index, child_value = min_child(heap, index)
    if child_index is None: return
    if child_value < value:
        heap[index] = child_value
        heap[child_index] = value
        if repeat:
            sift_down(heap, child_index)


def heapify(heap):
    for i in reversed(range(len(heap) // 2)):
        sift_down(heap, i)

def heappop(heap):
    if not heap: raise IndexError()
    if len(heap) == 1: return heap.pop()

    value = heap[0]
    last = heap.pop()
    heap[0] = last
    sift_down(heap, 0)
    return value


import random
if __name__ == '__main__':
    range_size = 1000
    n = 1000
    heap_list = [random.randrange(-2*range_size, 2*range_size) for _ in range(n)]
    print(sum(heap_list))
    heapify(heap_list)
    print(heap_list)
    print(sum(heap_list))
    while heap_list:
        print(heappop(heap_list))