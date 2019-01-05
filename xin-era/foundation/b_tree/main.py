

class Node:

    def __init__(self, keys=None, parent=None):

        # keys may temporarily be greater than 2
        self.keys = []
        self.children = []
        self.parent = parent
        self.keys.append(keys)

    def in_order(self):

        to_return = []
        if len(self.children) > 0:
            to_return += self.children[0].in_order()

        if self.keys:
            to_return += [self.keys[0]]

        if len(self.children) > 1:
            to_return += self.children[1].in_order()

        if self.keys and len(self.keys) > 1:
            to_return += [self.keys[1]]

        if len(self.children) > 2:
            to_return += self.children[2].in_order()

        return to_return


    def insert(self, value):

        if value in self.keys:
            return

        # Empty Tree
        if len(self.keys) == 0:
            self.keys += [value]


        # If there's children we need to insert farther down
        if self.children:
            for index, key in enumerate(self.keys):
                if value < key:
                    self.children[index].insert(value)
                    break
            else:
                if value > self.keys[-1]:
                    self.children[-1].insert(value)

        else:
            self.keys += [value]
            self.keys.sort()


            #CASE 0: We have less than 2 keys and we are done
            if len(self.keys) > 2:

                if self.parent is None:
                    # We are at the root and need to split
                    self.children += [Node(self.keys[0], parent=self)]
                    self.children += [Node(self.keys[2], parent=self)]
                    self.keys = [self.keys[1]]

                elif len(self.parent.keys) == 1:

                    # Move middle element to parent
                    pivot  = self.parent.keys[0]
                    left   = self.keys[0]
                    middle = self.keys[1]
                    right  = self.keys[2]

                    if middle > pivot:
                        self.parent.keys += [middle]
                        self.parent.children[1] = Node(left, parent=self.parent)
                        self.parent.children += [self]
                        self.keys = [right]
                    else:
                        cousin = self.parent.children[1]
                        self.parent.keys = [middle, pivot]
                        self.parent.children = [Node(left, parent=self.parent), self, cousin]
                        self.keys = [right]


                elif len(self.parent.keys) == 2:
                    # Everything is full, have to split parent
                    left   = self.keys[0]
                    middle = self.keys[1]
                    right  = self.keys[2]

                    self.parent.keys += [middle]
                    self.parent.keys.sort()

                    self.parent.children += [Node(left, parent=self.parent), Node(right, parent=self.parent)]
                    self.parent.children.remove(self)
                    self.parent.children.sort(key=lambda x : x.keys[0])

                    del left, middle, right

                    # Now we have 3 keys in parent and 4 children, so split

                    new_left = Node(self.parent.keys[0], parent=self.parent)
                    new_left.children = self.parent.children[:2]
                    for child in new_left.children:
                        child.parent = new_left

                    new_right = Node(self.parent.keys[2], parent=self.parent)
                    new_right.children = self.parent.children[2:]
                    for child in new_right.children:
                        child.parent = new_right

                    self.parent.children = [new_left, new_right]
                    self.parent.keys = [self.parent.keys[1]]







class BTree:
    """ 2-3 tree """

    def __init__(self):
        self.head = None

    def insert(self, key):

        if self.head is None:
            self.head = Node(key)
        else:
            self.head.insert(key)


    def to_list(self):
        """ in order traversal """
        return self.head.in_order()


import random
import unittest
class TestBSTMethods(unittest.TestCase):

    def test_head(self):
        tree = BTree()
        tree.insert(1)
        tree.insert(2)
        self.assertListEqual(tree.to_list(), [1,2])
        self.assertListEqual(tree.head.keys, [1,2])


    def test_simple_split(self):
        tree = BTree()
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)
        self.assertListEqual(tree.to_list(), [1,2, 3], "in_order test")
        self.assertListEqual(tree.head.keys, [2])
        self.assertListEqual(tree.head.children[0].keys, [1])
        self.assertListEqual(tree.head.children[1].keys, [3])


    def test_insert_4(self):
        tree = BTree()
        for key in [1,2,3,4]:
            tree.insert(key)
        self.assertListEqual(tree.to_list(), [1, 2, 3, 4], "in_order test")
        self.assertListEqual(tree.head.keys, [2])
        self.assertListEqual(tree.head.children[0].keys, [1])
        self.assertListEqual(tree.head.children[1].keys, [3, 4])


    def test_insert_5(self):
        tree = BTree()
        for key in [1,2,3,4,5]:
            tree.insert(key)
        self.assertListEqual(tree.to_list(), [1, 2, 3, 4, 5], "in_order test")
        self.assertListEqual(tree.head.keys, [2, 4])
        self.assertListEqual(tree.head.children[0].keys, [1])
        self.assertListEqual(tree.head.children[1].keys, [3])
        self.assertListEqual(tree.head.children[2].keys, [5])

    def test_insert_100_numbers(self):

        arr = list(range(100))
        tree = BTree()
        for key in arr:
            tree.insert(key)
        self.assertListEqual(tree.to_list(), list(range(100)), "in_order test")


    def test_insert_backwards(self):
        n = 100
        arr = list(reversed(range(n)))
        tree = BTree()
        for key in arr:
            tree.insert(key)
        self.assertListEqual(tree.to_list(), list(range(n)), "in_order test")


    def test_insert_random(self):
        n = 100
        arr =list(range(n))
        random.shuffle(arr)
        tree = BTree()
        for key in arr:
            tree.insert(key)
        self.assertListEqual(tree.to_list(), list(range(n)), "in_order test")



if __name__ == '__main__':
    test = True
    if test:
        unittest.main()
    else:
        keys = [1, 10, 9, 5, 4, 6, 2, 7, 10]
        m_tree = BTree()
        for key in keys:
            m_tree.insert(key)

        sorted_list = m_tree.to_list()
        print(sorted_list)
        print(m_tree.head.keys)
        print(m_tree.head.children[0].keys)
        print(m_tree.head.children[1].keys)
        print(m_tree.head.children[2].keys)

