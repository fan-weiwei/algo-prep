"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1

Your algorithm should run in O(n) time and uses constant extra space.

"""
from heapq import heapify, heappop
def solution2(arr):
    heapify(arr)
    next_int = 1

    # O(n log n)
    while len(arr) > 0:
        if heappop(arr) == next_int:
            next_int +=1
    return next_int


def solution(nums):
    n = len(nums)
    k = 0

    # eliminate non-positive and large
    for i, num in enumerate(nums):
        # n - (skipped) = n - (i - k)?
        if 0 < num and num <= n - (i - k):
            nums[k] = num
            k += 1


    for x in range(k):
        num = abs(nums[i])

        if nums[num - 1] > 0:
            nums[num - 1] *= -1
        else:
            k -= 1

    for i in range(k):
        if nums[i] >= 0:

            return i + 1

    return k + 1




import unittest
class SmallestTest(unittest.TestCase):
    def testExample1(self):
        arr = [1, 2, 0]
        result = 3
        self.assertEqual(solution(arr), result)


    def testExample2(self):
        arr = [3, 4, -1, 1]
        result = 2
        self.assertEqual(solution(arr), result)

    def testExample3(self):
        arr = [7, 8, 9, 11, 12]
        result = 1
        self.assertEqual(solution(arr), result)

    def testExample4(self):
        arr = [0,2,2,4,0,1,0,1,3]
        result = 5
        self.assertEqual(solution(arr), result)

    def testExample5(self):
        arr = [2, 1]
        result = 3
        self.assertEqual(solution(arr), result)


if __name__ == '__main__':
    unittest.main()