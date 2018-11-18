# Calculate the intersection of two rectangles


def interection(a , b):

    return 0



import unittest

class TestRectangles(unittest.TestCase):


    def test_same(self):
        a = {
            'left_x': 1,
            'bottom_y': 5,
            'width': 10,
            'height': 4,
        }

        self.assertEqual(interection(a, a), 40)

    def test_simple(self):
        a = {
            'left_x': 1,
            'bottom_y': 6,
            'width': 10,
            'height': 4,
        }

        b = {
            'left_x': 5,
            'bottom_y': 5,
            'width': 10,
            'height': 4,
        }

        self.assertEqual(interection(a,b), 6 * 3)


if __name__ == '__main__':
    unittest.main()