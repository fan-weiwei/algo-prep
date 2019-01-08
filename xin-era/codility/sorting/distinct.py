"""
Given an array A consisting of N integers, returns the number of distinct values in array A.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def solution(arr):
    return len(set(arr))

import unittest

class distinctTests(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual([], 0)

    def testSimple(self):
        self.assertEqual(solution([1, 2]), 2)
        self.assertEqual(solution([2, 2]), 1)

if __name__ == '__main__':
    unittest.main()