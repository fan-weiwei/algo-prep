"""
Assume this is a 2-3 Tree for now

Maximum keys are (2n-1) = 3
Minimum keys are (n) = 2

"""


class Node:

    def __init__(self):
        self.keys = []
        self.left = None
        self.middle = None
        self.right = None
        self.parent = None


    def __repr__(self):

        return self.keys.__repr__()

    def insert_key(self, key):
        self.keys += [key]
        self.keys.sort()

        if len(self.keys) == 3 and self.parent is None:
            left = Node()
            left.keys[0] = self.keys[0]
            right = Node()
            right.keys[0] = self.keys[2]

            self.children = [left, right]
            self.keys = self.keys[1:2]


class BTree:

    def __init__(self):
        self.head = None


    def insert(self, key):
        if self.head is None:
            self.head = Node()
            self.head.keys = [key]
            return
        else:
            self.head.insert_key(key)


    def __str__(self):
        if self.head is None:
            return 'Empty B Tree'


        string = 'B Tree: '
        string += self.head.__repr__()
        return string


if __name__ == '__main__':

    tree = BTree()

    tree.insert(2)
    tree.insert(1)
    tree.insert(6)

    print(tree)