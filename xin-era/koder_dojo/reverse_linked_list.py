class Node:

    def __init__(self, val : int, next : "Node" = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val



class LinkedList:

    def __init__(self, *values):
        self.head = None
        self.append(values)


    def append(self, *values):
        pass



if __name__ == '__main__':
    print('here')