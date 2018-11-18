def encode(arr):

    encoded = ''
    for word in arr:
        encoded += word.replace('|', '||') + '|0'

    return encoded

def decode(string):

    words = []
    word = ''

    index = 0
    while index < len(string):
        c1 = string[index]

        if c1 != '|':
            word += c1
            index += 1
            continue

        c2 = string[index + 1]
        if c2 == '0':
            words += [''.join(word)]
            word = ''
            index += 2
            continue

        if c2 == '|':
            word += '|'
            index += 2
            continue

    return words

import unittest

class TestSerializationMethods(unittest.TestCase):
    words = ['apple', 'banana', 'coconut']
    words2 = ['|', 'apple', 'coconut']
    words3 = ['|0', '||', '|']
    words4 = ['||0', '0||0', '|0|00||', '0', '|']
    words5 = ['']

    def test_easy(self):
        array = ['apple', 'banana', 'coconut']
        self.assertEqual(array, decode(encode(array)))

    def test_pipe(self):
        array = ['|', 'apple', 'coconut']
        self.assertEqual(array, decode(encode(array)))

    def test_break_characters(self):
        array = ['|0', '||', '|']
        self.assertEqual(array, decode(encode(array)))

    def test_trying_to_break(self):
        array = ['||0', '0||0', '|0|00||', '0', '|']
        self.assertEqual(array, decode(encode(array)))

    def test_empty(self):
        array = ['']
        self.assertEqual(array, decode(encode(array)))


if __name__ == '__main__':
    unittest.main()