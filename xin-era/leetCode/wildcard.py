"""
    Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

    s could be empty and contains only lowercase letters a-z
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

    IMPORTANT: The matching should cover the entire input string (not partial).

"""

def is_match2(string, pattern):
    n = len(string)
    i = 0
    j = 0
    s_star = 0
    p_star = -1

    while i < n:
        if j < len(pattern) and (string[i] == pattern[j] or pattern[j] == '?'):
            i += 1
            j += 1
        elif j < len(pattern) and pattern[j] == '*':
            s_star = i
            p_star = j
            j += 1
        elif p_star != -1:
            s_star += 1
            i = s_star
            j = p_star + 1
        else:
            return False

    while j < len(pattern) and pattern[j] == '*':
        j += 1
    return True if j == len(pattern) else False


def is_match(string, pattern):

    # weird edge case, but ok
    if string != '' and pattern == '': return False

    pattern = pattern.split("*")
    s_index = 0

    for subset in pattern:
        found = False
        p_index = 0
        while not found:
            # check if we matched the whole pattern
            if p_index == len(subset):

                found = True
                continue

            # check if we ran out of string to complete match
            elif s_index == len(string):
                return False

            # regular pattern matching
            else:
                if string[s_index] != subset[p_index] and subset[p_index] != '?':
                    # start over search
                    s_index = s_index - p_index + 1
                    p_index = 0
                else:
                    s_index += 1
                    p_index += 1

    # force end to match pattern [-1]
    # we might be able to delay matching in order to use the entire string
    if s_index < len(string) and pattern[-1] != '':

        # already used pattern for start
        if len(pattern) == 1:
            return False

        final = pattern[-1]
        for offset, char in enumerate(reversed(final)):
            if string[-(offset + 1)] != char and char != '?':
                return False

    return True


import unittest

class WildcardTests(unittest.TestCase):

    def testSimple(self):
        self.assertTrue(is_match('abc', 'a*c'))


    def testEndBoundary(self):
        self.assertTrue(is_match('abcc', 'a*c'))


    def testEndTooSoon(self):
        self.assertFalse(is_match('ab', 'a*c'))


    def testQuestionMark(self):
        self.assertTrue(is_match('abc', 'a?c'))


    def testEndWithWildcard(self):
        self.assertTrue(is_match('abc', 'a*'))
        self.assertTrue(is_match('abc', 'a*b*'))

    def testComplex(self):
        self.assertTrue(is_match('abcdefabc', '*a?c*?a?c*'))

    def testComplex2(self):
        self.assertTrue(is_match('aaaaaaaaaa', 'a**a??a?*??a'))

    def testExample(self):
        self.assertFalse(is_match('aa', 'a'))

    def testExample2(self):
        self.assertFalse(is_match('a', 'aa'))

    def testExample3(self):
        self.assertFalse(is_match('acdcb', 'a*c?b'))


    def testEdgeCase1(self):
        self.assertTrue(is_match('', ''))

    def testEdgeCase2(self):
        self.assertFalse(is_match('a', ''))

    def testExample4(self):
        self.assertTrue(is_match('aac', '*ac'))


if __name__ == '__main__':
    unittest.main()