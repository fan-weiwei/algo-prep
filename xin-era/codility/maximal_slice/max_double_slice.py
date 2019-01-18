"""

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.
The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

given a non-empty array A consisting of N integers, returns the maximal sum of any double slice

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].

"""

def solution(arr):
    n = len(arr)
    assert(n >= 3)

    # calc max ending in O(n)
    # calc max starting in O(n)
    # iterate through once more for pivot in O(n)

    # also I solved the wrong problem haha

    max_ending = [arr[0]]
    for x in arr[1:]:
        max_ending += [max(x, max_ending[-1] + x)]

    max_starting = [arr[-1]]
    for x in reversed(arr[:-1]):
        max_starting += [max(x, max_starting[-1] + x)]
    max_starting = list(reversed(max_starting))

    print(max_ending)
    print(max_starting)

    result = 0
    for pivot in range(1,n-1):
        working_sum = max_ending[pivot - 1] + max_starting[pivot + 1]
        #print(working_sum)
        if working_sum > result:
            result = working_sum

    return result

import unittest
class DoubleSliceTest(unittest.TestCase):

    def testExample(self):
        arr = [3, 2, 6, -1, 4, 5, -1, 2]
        self.assertEqual(solution(arr), 17)

    def testMinimal(self):
        arr = [1,2,3]
        self.assertEqual(solution(arr), 0)


    def testComplex(self):
        arr = [1,2,3, -30, 10, -20, 10, 2, 10]
        self.assertEqual(solution(arr), 32)

if __name__ == '__main__':
    unittest.main()