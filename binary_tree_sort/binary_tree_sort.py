unsorted_array = [5, 6, 0, 1, 2, 7, 6, 5, 1, 10, 11, 12, 67, 2, 6, 9, 32]

class Node():

    __slots__ = ['value', 'left', 'right']

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, x):

        if x <= self.value:
            if self.left is None:
                self.left = Node(x)
            else:
                self.left.add(x)

        if x > self.value:
            if self.right is None:
                self.right = Node(x)
            else:
                self.right.add(x)

    def sorted(self):

        result = []
        if self.left is not None:
            result += self.left.sorted()

        result += [self.value]

        if self.right is not None:
            result += self.right.sorted()

        return result


def bst_sort(arr):
    if len(arr) <= 1: return arr

    root = Node(arr[0])

    for x in arr[1:]:
        root.add(x)

    return root.sorted()

print(bst_sort(unsorted_array))

import unittest

class TestBSTMethods(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(bst_sort(unsorted_array), [0, 1, 1, 2, 2, 5, 5, 6, 6, 6, 7, 9, 10, 11, 12, 32, 67])

    def test_single_element(self):
        self.assertEqual(bst_sort([0]), [0])

    def test_empty(self):
        self.assertEqual(bst_sort([]), [])


if __name__ == '__main__':
    unittest.main()
