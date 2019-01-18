"""

Given elements in a stream, find median
"""

from heapq import heappop, heappush
class Median:
    """
    left is a record of negative offset from median
    right is positive offset

    """

    def __init__(self):
        self.left = []
        self.right = []

    def add(self, value):
        if len(self.right) == 0:
            self.right = [value]
            return

        head = self.right[0]
        if value > head:
            heappush(self.right, value)
        else:
            heappush(self.left, -value)


        balance = len(self.right) - len(self.left)
        if balance >= 2:
            heappush(self.left, -heappop(self.right))
        if balance <= -1:
            heappush(self.right, -heappop(self.left))


    def value(self):
        if len(self.right) == 0:
            return None

        balance = len(self.right) - len(self.left)
        if balance == 1:
            return float(self.right[0])
        else:
            return (-self.left[0] + self.right[0]) / 2

    def to_list(self):
        return [ -x for x in reversed(self.left)] + self.right




import unittest
import numpy
import random

class MedianTests(unittest.TestCase):

    def assertMediansEqual(self, arr):
        median = Median()

        for x in arr:
            median.add(x)

        true_median = numpy.median(arr)
        self.assertEqual(median.value(), true_median)


    def testSimple(self):
        self.assertMediansEqual([0, 1, 2])


    def testRandomLarge(self):
        random_list = [random.randrange(-100, 100) for _ in range(1000)]
        self.assertMediansEqual(random_list)




if __name__ == '__main__':
    unittest.main()
