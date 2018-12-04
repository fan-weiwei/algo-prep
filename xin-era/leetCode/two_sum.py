import unittest


def solution(nums, target):

    mapping = {}

    for index, num in enumerate(nums):
        if target - num in mapping:
            return [mapping[target - num], index]
        else:
            mapping[num] = index

    raise ValueError


if __name__ == '__main__':
    unittest.main()

class SolutionTests(unittest.TestCase):

    def test_example(self):
        input = [2, 7, 11, 15]
        target = 9

        self.assertEqual([0, 1], solution(input, target))


    def test_unsorted(self):
        input = [2, 15, 7, 11]
        target = 9

        self.assertEqual([0, 2], solution(input, target))


    def test_no_solution(self):
        input = [2, 15, 11]
        target = 9
        with self.assertRaises(ValueError):
            solution(input, target)