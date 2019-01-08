"""

    given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs.
     The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

    N is an integer within the range [0..100,000];
    each element of array A is an integer within the range [0..2,147,483,647].

    discs contain their borders


"""

# This problem isn't actually 2-D, if there's an intersection it also intersects on the x-axis
# Nothing below 0 matters, only integer co-ordinates matter
# we need to sort


from heapq import heappop, heappush
def solution(arr):

    if not arr:
        return 0

    finish = lambda x : x[0] + x[1]

    arr = list(enumerate(arr))
    # sort by finish time
    arr.sort(key=finish, reverse=True)

    end = finish(arr[0])
    heap = []
    total = 0

    for item in arr:
        while len(heap) > 0 and end - heap[0] > finish(item):
            heappop(heap)
        total += len(heap)
        heappush(heap, end - (item[0] - item[1]))

        if total > 10000000:
            return -1

    return total

import unittest
class DiscTests(unittest.TestCase):

    def testExample(self):
        arr = [1, 5, 2, 1, 4, 0]
        self.assertEqual(solution(arr), 11)

    def testSimple(self):
        arr = [1, 1, 1]
        self.assertEqual(solution(arr), 3)


    def testEmpty(self):
        arr = []
        self.assertEqual(solution(arr), 0)


    def testSingle(self):
        arr = [1]
        self.assertEqual(solution(arr), 0)



if __name__ == '__main__':
    unittest.main()