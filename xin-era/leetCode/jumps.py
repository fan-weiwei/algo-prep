

def jump1(arr):
    """
    :type arr: List[int]
    :rtype: int
    """

    # O(n^2)
    jumps = [0]
    for x in reversed(arr[:-1]):
        if x == 0:
            jumps.append(float('inf'))
        else:
            jumps.append(min(jumps[-x:]) + 1)

    return jumps[-1]

def jump(nums):

    # O(n)
    n = len(nums)
    if not nums or n == 1:
        return 0

    local_max = 0
    jumps = 0
    global_max = 0
    cursor = 0

    while global_max < n:
        jumps += 1

        while cursor <= global_max:
            local_max = max(local_max, nums[cursor] + cursor)
            if local_max >= n - 1:
                return jumps
            cursor += 1
        global_max = local_max

    return 0


import unittest
class JumpTest(unittest.TestCase):

    def testExample(self):
        test = [2, 3, 1, 1, 4]
        result = 2
        self.assertEqual(jump(test), result)


    def testSingleton(self):
        test = [2]
        result = 0
        self.assertEqual(jump(test), result)


    def testLargeFirst(self):
        test = [10,1]
        result = 1
        self.assertEqual(jump(test), result)

    def testMiddleZeros(self):
        test = [1,2,0,1]
        result = 2
        self.assertEqual(jump(test), result)

    def testExample2(self):
        test = [2,0,2,4,6,0,0,3]
        result = 3
        self.assertEqual(jump(test), result)


if __name__ == '__main__':
    # TODO: A*
    unittest.main()
    #test = [2, 0, 2, 4, 6, 0, 0, 3]
    #result = 3
    #jump(test)