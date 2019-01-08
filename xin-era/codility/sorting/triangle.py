"""

given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].

(solution [10, 2, 5, 1, 8, 20]) == 1
(solution [10, 50, 5, 1]) = 0

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647]

"""

def solution(arr):
    arr = [x for x in arr if x > 0]
    if len(arr) < 3:
        return 0

    # Given three numbers, we only have to ensure that 2 of them are greater than the maximum element
    # If a solution exists with a given maximum element, the elements directly prior in order are also solutions
    arr.sort(reverse=True)
    for index, item in enumerate(arr[:-2]):
        if item < arr[index + 1] + arr[index + 2]:
            return 1

    return 0

import unittest
class triangleTests(unittest.TestCase):

    def testExample(self):
        self.assertEqual(solution([10, 2, 5, 1, 8, 20]), 1)
        self.assertEqual(solution([10, 50, 5, 1]), 0)

    def testSmall(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([1]), 0)
        self.assertEqual(solution([1, 2]), 0)

    def testNegative(self):
        self.assertEqual(solution([10, -10, 10]), 0)
        self.assertEqual(solution([10, -10, 2, 1]), 0)



if __name__ == '__main__':
    unittest.main()