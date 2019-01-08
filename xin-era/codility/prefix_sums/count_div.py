"""
    def solution(A, B, K)
    len { i : A ≤ i ≤ B, i mod K = 0 }


    A and B are integers within the range [0..2,000,000,000];
    K is an integer within the range [1..2,000,000,000];
    A ≤ B.


"""

def solution2(a, b, k):
    div = (b - a + 1) // k
    remainder = (b - a + 1) % k + (a - 1) % k
    if remainder >= k:
        div += 1
    return div

def solution(a, b, k):
    lower = a -1
    delta = b - lower
    return (delta + lower % k) // k



import unittest
class SolutionTests(unittest.TestCase):

    def testSimple(self):
        self.assertEqual(solution(0, 1, 1), 2)
        self.assertEqual(solution(1, 1, 1), 1)
        self.assertEqual(solution(0, 1, 2), 1)
        self.assertEqual(solution(1, 1, 2), 0)
        self.assertEqual(solution(5, 5, 5), 1)
        self.assertEqual(solution(4, 5, 5), 1)
        self.assertEqual(solution(4, 6, 5), 1)
        self.assertEqual(solution(6, 9, 5), 0)




if __name__ == '__main__':
    unittest.main()
    print('here')