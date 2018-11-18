# Your quirky boss collects rare, old coins...

def change_com(amount, denom):

    if amount == 0: return 1
    if len(denom) == 0: return 0

    result = 0
    remainder = amount
    largest = denom[0]
    while remainder >= 0:
        result += change_com(remainder, denom[1:])
        remainder -= largest

    return result


import unittest

class TestChange(unittest.TestCase):

    def test_single(self):
        self.assertEqual(change_com(1, [1]), 1)

    def test_simple_3(self):
        self.assertEqual(change_com(3, [1,2]),2)

    def test_simple_4(self):
        self.assertEqual(change_com(4, [1,2, 3]),4)

    def test_simple_4(self):
        self.assertEqual(change_com(25, [1, 5, 10, 25]), 13)

    # define 1 way to make 0 amount, that is include nothing
    def test_zero(self):
        self.assertEqual(change_com(0, [1, 5, 10]), 1)
        # define 1 way to make 0 amount, that is include nothing

    def test_impossible(self):
        self.assertEqual(change_com(1, [3]), 0)

    def test_impossible2(self):
        self.assertEqual(change_com(5, [4,2]), 0)

    def test_impossible3(self):
        self.assertEqual(change_com(5, [2,4,6,7]), 0)


if __name__ == '__main__':
    unittest.main()