import collections

class Node:


    __slots__ = ['value', 'left', 'right', 'height', 'depth']

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.depth = 0


    def traverse(self, onTraverse):

        if self.left:
            self.left.traverse(onTraverse)

        onTraverse(self)

        if self.right:
            self.right.traverse(onTraverse)

    def traverse_preorder(self, onTraverse):

        onTraverse(self)

        if self.left:
            self.left.traverse_preorder(onTraverse)

        if self.right:
            self.right.traverse_preorder(onTraverse)

    def insert(self, value):

        print('inserting {} at {}'.format(value, self.value))

        if self.value > value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
                self.left.depth = self.depth + 1
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
                self.right.depth = self.depth + 1


        # After insert

        l_height = 0
        r_height = 0
        if self.left:  l_height = self.left.height
        if self.right: r_height = self.right.height

        #print('   {} {}'.format(l_height, r_height))
        self.height = 1 + max(l_height, r_height)

        balance = l_height - r_height

        # left left
        if balance > 1 and self.value > value:
            #self.rotate_right()
            pass

        # right right
        if balance < -1 and self.value <= values:
            #seld.rotate_left()
            pass

        # left right
        if balance > 1 and self.value > value:
            #self.l
            pass

        # right left
        if balance < -1 and self.value <= values:


            pass




    







class AVL:

    def __init__(self):
        self.head = None


    def insert(self, value):

        if not self.head:
            self.head = Node(value)
        else:
            self.head.insert(value)



    def print_tree(self):

        if self.head is None:
            print('empty\n')
            return

        def print_node(x):
            for _ in range(x.depth):
                print('_', end='')
            print('[{:>2}]'.format(x.value))

        self.head.traverse_preorder(print_node)






if __name__ == '__main__':


    tree = AVL()
    tree.print_tree()

    #values = [15, 1, 2, 0]
    #values = [15, 1, 2, 17, 8, 9, 7]
    values = [15, 1, 2, 17, 8, 9, 7, 2, -1, 0, 20]

    for value in values:
        tree.insert(value)


    tree.print_tree()
    tree.head.traverse(lambda x : print(x.value))
