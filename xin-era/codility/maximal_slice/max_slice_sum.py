"""

given an array A consisting of N integers, returns the maximum sum of any slice of A

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].

"""

def solution(arr):
    if not arr: raise ValueError()

    working_sum = arr[0]
    result = arr[0]
    for x in arr[1:]:
        working_sum = max(x, working_sum + x)
        if working_sum > result:
            result = working_sum

    return result

import unittest
class SliceTests(unittest.TestCase):

    def testExample(self):
        arr = [3, 2, -6, 4, 0]
        self.assertEqual(solution(arr), 5)


    def testSimple(self):
        arr = [3, 2, 5]
        self.assertEqual(solution(arr), 10)


    def testNegative(self):
        arr = [-3, -2, -5]
        self.assertEqual(solution(arr), -2)


    def testComplex(self):
        arr = [3, 2, -6, 4, 0, 10, -2, 4, -6, -2, 2]
        self.assertEqual(solution(arr), 16)


    def testOnes(self):
        arr = [1, 1, 1, 1, 1]
        self.assertEqual(solution(arr), 5)



    def testEmpty(self):
        arr = []
        self.assertRaises(ValueError, solution, arr)


if __name__ == '__main__':
    unittest.main()
    print('here')

