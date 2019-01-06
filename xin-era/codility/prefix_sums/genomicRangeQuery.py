"""

Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4,

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.
 There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers.
  The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained
  in the DNA sequence between positions P[K] and Q[K] (inclusive).

  N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.


"""

def solution(S, P, Q):

    n = len(S)
    prefix = [[0,0,0,0]] * (n + 1)
    for index in range(1, n + 1):
        prior = prefix[index - 1].copy()
        char = S[index - 1]
        if char == 'A':
            prior[0] += 1
        if char == 'C':
            prior[1] += 1
        if char == 'G':
            prior[2] += 1
        if char == 'T':
            prior[3] += 1

        prefix[index] = prior


    result = []

    for p, q in zip(P, Q):
        delta = list(map(lambda x: x[0] - x[1], zip(prefix[q + 1], prefix[p])))
        for index, val in enumerate(delta):
            if val != 0:
                result += [index + 1]
                break

    return result

import unittest
class solutionTest(unittest.TestCase):

    def testExample(self):
        s = 'CAGCCTA'
        p = [2, 5, 0]
        q = [4, 5, 6]
        self.assertEqual(solution(s, p, q), [2, 4, 1])


if __name__ == '__main__':
    unittest.main()