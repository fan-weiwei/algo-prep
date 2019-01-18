"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it is able to trap after raining.


"""


def solution2(arr):

    # Problem here is that it's O(n)
    if not arr: return 0
    trapped = 0

    max_left = [0]
    for item in arr[:-1]:
        max_left.append(max(max_left[-1], item))

    max_right = [0]
    for item in reversed(arr[1:]):
        max_right.append(max(max_right[-1], item))
    max_right.reverse()

    for index, item in enumerate(arr):
        if item < 0: raise ValueError()
        height = min(max_left[index], max_right[index]) - item
        height = max(height, 0)
        trapped += height

    return trapped


def solution(arr):
    if not arr or len(arr) < 3:
        return 0

    trapped = 0

    left = 0
    right = len(arr) -1

    max_left = 0
    max_right = 0

    while left < right:
        max_left = max(arr[left], max_left)
        max_right = max(arr[right], max_right)

        if max_left <= max_right:
            trapped += max_left - arr[left]
            left += 1
        else:
            trapped += max_right - arr[right]
            right -= 1

    return trapped



import unittest
class RainwaterTests(unittest.TestCase):

    def testEmpty(self):
        arr = []
        result = 0
        self.assertEqual(solution(arr), result)

    def testSingleton(self):
        arr = [1]
        result = 0
        self.assertEqual(solution(arr), result)

    def testTwo(self):
        arr = [1, 2]
        result = 0
        self.assertEqual(solution(arr), result)


    def testSimple(self):
        arr = [1, 0, 1]
        result = 1
        self.assertEqual(solution(arr), result)

    def testExample(self):
        arr = [0,1,0,2,1,0,1,3,2,1,2,1]
        result = 6
        self.assertEqual(solution(arr), result)

    def testLargeValue(self):
        arr = [0,1,0,100,2]
        result = 1
        self.assertEqual(solution(arr), result)

    def testLeadingZeros(self):
        arr = [0,0,0,0,0,1,0,0,0]
        result = 0
        self.assertEqual(solution(arr), result)

    def testAllZero(self):
        arr = [0, 0, 0, 0]
        result = 0
        self.assertEqual(solution(arr), result)

    def testUniform(self):
        arr = [2,2,2,2]
        result = 0
        self.assertEqual(solution(arr), result)

    def testEdges(self):
        arr = [100, 0, 100]
        result = 100
        self.assertEqual(solution(arr), result)


    def testUnequal(self):
        arr = [100, 0, 2]
        result = 2
        self.assertEqual(solution(arr), result)



if __name__ == '__main__':
    unittest.main()
    #print(solution([0,1,2,1]))
    print('here')