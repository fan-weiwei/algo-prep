import math
import random

class AVL:

    __slots__ = ['key', 'left', 'right', 'height', 'balance', 'balancing']

    def __init__(self, key=None, balancing=True):
        self.key = key
        self.left  = None
        self.right = None
        self.height = 0
        self.balance = 0
        self.balancing = True

    def insert_right(self, key):
        if self.right is None:
            self.right = AVL(key)
        else:
            self.right.insert(key)

    def insert_left(self, key):
        if self.left is None:
            self.left = AVL(key)
        else:
            self.left.insert(key)

    def update_balance(self):

        ## update heights
        l_height = 0
        if self.left is not None:
            l_height = self.left.height

        r_height = 0
        if self.right is not None:
            r_height = self.right.height

        self.height = max(l_height, r_height) + 1

        ## find balance
        self.balance = l_height - r_height



    def insert(self, key):
        if self.key is None:
            self.key = key
        elif key > self.key:
            self.insert_right(key)
        else:
            self.insert_left(key)

        self.update_balance()

        if not self.balancing:
            return

        ## check balance
        if self.balance > 1:
            if self.left.balance >= 0:

                # left left
                self.rotate_right()
            else:

                # left right
                self.left.rotate_left()
                self.rotate_right()

        elif self.balance < -1:
            # right heavy
            if self.right.balance <= 0:

                # right right
                self.rotate_left()
            else:

                # right left
                self.right.rotate_right()
                self.rotate_left()


    def rotate_left(self):

        if self.right is None:
            raise RuntimeError()

        new_left = AVL(self.key)
        new_left.left = self.left
        new_left.right = self.right.left

        new_right = self.right.right

        new_key = self.right.key

        self.left = new_left
        self.right = new_right
        self.key = new_key


        self.left.update_balance()
        self.update_balance()


    def rotate_right(self):

        if self.left is None:
            raise RuntimeError()

        new_right = AVL(self.key)
        new_right.right = self.right
        new_right.left = self.left.right

        new_left = self.left.left

        new_key = self.left.key

        self.left = new_left
        self.right = new_right
        self.key = new_key


        self.right.update_balance()
        self.update_balance()


    def as_list(self):

        list = []
        if self.left is not None:
            list += self.left.as_list()

        list += [self.key]
        if self.right is not None:
            list += self.right.as_list()

        return list

    def __str__(self):
        return self.as_list().__str__()


import time
if __name__ == '__main__':

    # values = [15, 1, 2, 17, 8, 9, 7, 2, -1, 0, 20, 13, 16, 3]

    number_of_values = 10000
    values = [random.randrange(-20000,20000) for _ in  range(number_of_values)]

    start = time.clock()
    tree = AVL()
    for value in values:
        tree.insert(value)
    end = time.clock()

    unbalanced_tree = AVL(balancing=False)

    for value in values:
        unbalanced_tree.insert(value)

    list_1 = tree.as_list()
    list_2 = tree.as_list()
    for i in range(number_of_values):
        assert(list_1[i] == list_2[i])


    min_height = math.log(tree.as_list().__len__(), 2)

    #print(tree)
    print('Actual Height {}'.format(tree.height))
    print('Minimum Height {}'.format(min_height))
    print('Time {}'.format(end - start))

    print('here')
