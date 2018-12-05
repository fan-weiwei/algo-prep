import random


def heapify(heap):

    for i in reversed(range(0, len(heap) // 2)):
        sift_down(heap, i)

def sift_down(heap, index):

    while index < len(heap) // 2:

        children = [2 * index + 1, 2 * index + 2]
        children = [(x, heap[x]) for x in children if x < len(heap)]
        children.sort(key=lambda x: x[1], reverse=False)

        # we are guaranteed to have a value here since 2 * index + 1 < len(heap)
        c_index, c_value = children[0]

        if c_value < heap[index]:

            # then swap them
            temp = heap[index]
            heap[index] = c_value
            heap[c_index] = temp

            index = c_index
        else:
            break

def sift_up(heap, index):

    while index is not None:
        p_index = parent_index(index)

        if heap[index] < heap[p_index]:
            temp = heap[index]
            heap[index] = heap[p_index]
            heap[p_index] = temp

            index = p_index

        else:
            break



def heap_insert(heap, item):
    heap.append(item)
    sift_up(heap, len(heap) - 1)

def heap_pop(heap):
    if len(heap) == 0:
        return None

    last = heap.pop()
    if len(heap) == 0:
        return last


    min_val = heap[0]
    heap[0] = last

    sift_down(heap, 0)

    return min_val


def parent_index(i):
    if i == 0:
        return None
    return (i - 1)  // 2

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2



import time
if __name__ == '__main__':

    n = 10000
    values = [random.randrange(-2*n,2*n) for _ in  range(n)]
    #values = [6, 5, 4, 3, 2, 1, 0]
    print(values)
    start = time.clock()
    heapify(values)


    sorted = []
    for _ in range(len(values)):
        sorted.append(heap_pop(values))

    end = time.clock()

    print(sorted)
    print('Time {}'.format(end - start))