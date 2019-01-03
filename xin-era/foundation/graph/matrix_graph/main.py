class Graph:

    def __init__(self, n):
        self.adjMatrix = [[-1] * n for _ in range(n)]
        self.n = n

    def add_edge(self, i, j, cost=0):
        if i not in range(self.n):
            raise IndexError()

        if j not in range(self.n):
            raise IndexError()

        self.adjMatrix[i][j] = cost
        self.adjMatrix[j][i] = cost


if __name__ == '__main__':
    n = 5
    graph = Graph(n)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    