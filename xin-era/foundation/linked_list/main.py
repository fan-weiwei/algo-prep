class Node:

    __slots__ = ['value', 'next']

    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, value):
        self.last.next = Node(value)

    @property
    def last(self):
        if self.next is None:
            return self
        else:
            return self.next.last

    def __len__(self, count=0):
        count += 1
        if self.next is None:
            return count
        else:
            return self.next.__len__(count)

    def __getitem__(self, index):
        if index < 0:
            return ValueError()

        if index == 0:
            return self.value

        if self.next is None:
            return ValueError()
        else:
            return self.next.__getitem__(index - 1)


class LinkedList:

    __slots__ = ['head']

    def __init__(self, *args):
        self.head = None
        for arg in reversed(args):
            node = Node(arg)
            node.next = self.head
            self.head = node

    def __iter__(self):
        return LinkedListIterator(self.head)

    def append(self, *args):
        to_append = LinkedList(*args).head
        self.head.last.next = to_append


    def __len__(self):
        return self.head.__len__()


    def __getitem__(self, item):
        return self.head.__getitem__(item)



class LinkedListIterator:

    def __init__(self, head):
        self.head = head

    def __next__(self):

        if self.head is None:
            raise StopIteration()
        else:
            value = self.head.value
            self.head = self.head.next
            return value



if __name__ == '__main__':

    linked_list = LinkedList(1)
    linked_list.append(2, 3)
    linked_list.append(4)

    print(f'Length of list: {len(linked_list)}')
    print(f'id()   :{id(linked_list)}')
    print(f'type() :{type(linked_list)}')


    print(f'Second Item : {linked_list[1]}')

    

    for value in linked_list:
        print(value)