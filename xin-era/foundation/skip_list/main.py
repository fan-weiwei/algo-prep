import random
class Node:

    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

class SkipList:

    def __init__(self, max_level, p):
        self.MAX_LEVEL = max_level
        self.p = p
        self.header = self.createNode(self.MAX_LEVEL, -1)
        self.level = 0

    def createNode(self, level, key):
        n = Node(key, level)
        return n

    def randomLevel(self):
        level = 0
        while random.random() < self.p and level < self.MAX_LEVEL:
            level += 1
        return level

    def insertElement(self, key):

        update = [None] * (self.MAX_LEVEL + 1)
        current = self.header

        ''' 
               start from highest level of skip list 
               move the current reference forward while key  
               is greater than key of node next to current 
               Otherwise inserted current in update and  
               move one level down and continue search 
               '''

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        print(self.level)
        '''  
        reached level 0 and forward reference to  
        right, which is desired position to  
        insert key. 
        '''

        current = current.forward[0]
        ''' 
        if current is NULL that means we have reached 
          to end of the level or current's key is not equal 
          to key to insert that means we have to insert 
          node between update[0] and current node 
        '''
        if current is None or current.key != key:
            # Generate a random level
            random_level = self.randomLevel()

            ''' 
            If random level is greater than list's current 
            level (node with highest level inserted in  
            list so far), initialize update value with reference 
            to header for further use 
            '''

            if random_level > self.level:
                for i in range(self.level + 1, random_level + 1):
                    update[i] = self.header
                self.level = random_level

            # create new node with random level generated
            n = self.createNode(random_level, key)

            # insert node by rearranging references
            for i in range(random_level + 1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

            print("Successfully inserted key {}".format(key))

    def displayList(self):
        print("\n*** Skip List ***")
        head = self.header
        for level in range(self.level + 1):
            print("Level {}: ".format(level), end=" ")
            node = head.forward[level]
            while node is not None:
                print(node.key, end=" ")
                node = node.forward[level]
            print("")

if __name__ == '__main__':
    lst = SkipList(3, 0.5)
    lst.insertElement(3)
    lst.insertElement(6)
    lst.insertElement(7)
    lst.insertElement(9)
    lst.insertElement(12)
    lst.insertElement(19)
    lst.insertElement(17)
    lst.insertElement(26)
    lst.insertElement(21)
    lst.insertElement(25)
    lst.displayList()

