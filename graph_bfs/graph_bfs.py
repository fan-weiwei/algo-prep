


class Graph():


    def __init__(self):
        self.nodes = {}

    def addEdge(self, a, b):

        if a not in self.nodes:
            self.nodes[a] = set()

        if b not in self.nodes:
            self.nodes[b] = set()


        self.nodes[a].add(b)
        self.nodes[b].add(a)

    def BFS(self, start):


        visited = set()
        stack = [start]

        while stack:

            current = stack.pop()

            if current in visited: continue
            visited.add(current)
            print("on node: {}".format(current))

            for next in self.nodes[current]:
                stack.append(next)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)