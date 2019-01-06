"""
Given a non-empty array A of N integers in [0,1] return number of passing cars
The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.


Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""

def solution(arr):

    east_count = 0
    total = 0
    for bit in arr:
        if bit == 0:
            east_count +=1
        if bit == 1:
            total += east_count

        if total > 10 ** 9:
            return -1

    return total


def prefix_solution(arr):
    n = len(arr)
    prefix = [0] * (n+1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]

    total = 0


    for i in range(n):
        if arr[i] == 0:
            total += (prefix[n] - prefix[i])

    return total


import unittest

class SolutionTest(unittest.TestCase):

    def testSimple(self):
        arr = [0]
        answer = 0
        self.assertEqual(prefix_solution(arr), answer)


    def testPassing1(self):
        arr = [0, 1]
        answer = 1
        self.assertEqual(prefix_solution(arr), answer)


    def testExample(self):
        arr = [0, 1, 0, 1, 1]
        answer = 5
        self.assertEqual(prefix_solution(arr), answer)



if __name__ == '__main__':
    unittest.main()