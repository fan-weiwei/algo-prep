"""
given a non-empty array A, returns the value of the maximal product of any triplet.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].

"""

def solution(arr):
    max_three = []
    negative_two = []

    for val in arr:
        if val < 0 and len(negative_two) < 2:
            negative_two += [val]
            negative_two.sort()
        elif val < 0 and val < negative_two[-1]:
            negative_two[-1] = val
            negative_two.sort()


        if len(max_three) < 3:
            max_three += [val]
            max_three.sort()
        elif val > max_three[0]:
            max_three[0] = val
            max_three.sort()

    case1 = max_three[0] * max_three[1] * max_three[2]

    if len(negative_two) == 2:
        case2 = negative_two[0] * negative_two[1] * max_three[2]
        return max(case1, case2)

    return case1


import unittest
class tripleTest(unittest.TestCase):

    def testSimple(self):
        self.assertEqual(solution([1, 1, -1]), -1)
        self.assertEqual(solution([1, 1, 1]), 1)
        self.assertEqual(solution([9,8,7,5]), 9 * 8 * 7)
        self.assertEqual(solution([9,8,7,-6, -10]), 9 * -6 * -10)


if __name__ == '__main__':
    unittest.main()

