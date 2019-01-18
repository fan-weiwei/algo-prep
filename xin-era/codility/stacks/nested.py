"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.

     given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

     N is an integer within the range [0..200,000];
    string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".



"""


def solution(s):
    stack = []
    inverse = { '(' : ')', '{' : '}', '[' : ']'}

    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if not stack:
                return 0

            if inverse[stack[-1]] == char:
                stack.pop()
            else:
                return 0
        else:
            continue
    else:
        if stack:
            return 0

    return 1

import unittest
class NestedTests(unittest.TestCase):

    def testEmpty(self):
        s = ''
        self.assertEqual(solution(s), 1)

    def testSimpleMatached(self):
        s = '({[]})'
        self.assertEqual(solution(s), 1)


    def testSimpleUnmatached(self):
        s = '({[])'
        self.assertEqual(solution(s), 0)


    def testSimpleUnclosed(self):
        s = '('
        self.assertEqual(solution(s), 0)

    def testComplex(self):
        s = '(){[]}[({}())]'
        self.assertEqual(solution(s), 1)


    def testComplexUnmatched(self):
        s = '(){[]}[({())]'
        self.assertEqual(solution(s), 0)


if __name__ == "__main__":
    unittest.main()