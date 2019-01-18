"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""

def simple_median(x):
    n = len(x)
    if n % 2 == 0:
        return (x[ n // 2 - 1] + x[n //2]) /2
    else:
        return x[n // 2]


def median(x, y):
    m = len(x)
    n = len(y)
    is_odd = (m + n) % 2 == 1

    # indicies
    left_x = 0
    left_y = 0

    x_value = x[0]
    y_value = y[0]


    target_count = None
    if is_odd:
        target_count = (m + n) // 2
    else:
        target_count = (m + n - 2) // 2

    total_count = left_x + left_y

    while total_count != target_count:

        if total_count < target_count:
            # we need to increase either left_x or right_x
            if x_value < y_value:
                # we need to increase left_x





        # then update values
        x_value = x[left_x]
        y_value = y[left_y]







    else:

        return 0





import unittest

class MedianTests(unittest.TestCase):

    def testExample1(self):
        x = [1, 3]
        y = [2]
        self.assertEqual(median(x,y), 2.0)

    def testExample2(self):
        x = [1, 2]
        y = [3, 4]
        self.assertEqual(median(x,y), 2.5)

if __name__ == '__main__':
    x = [1, 2, 5, 6, 8]
    y = [3, 4, 7, 8]

    print(simple_median(x))
    print(median(x, y))


