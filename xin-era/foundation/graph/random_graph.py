import random


class Graph:

    def __init__(self, p, n):

        assert(n > 1)

        self.n = n
        self.matrix = [[-1] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                value = 0
                if random.random() < p:
                    value = 1
                self.matrix[i][j] = value

    def __repr__(self):
        return self.matrix.__repr__()

    def __str__(self):
        return self.matrix.__str__()

    def is_connected(self):
        connected = False

        visited = {0}
        stack = [0]

        while stack and not connected:

            v = stack.pop()
            for x in range(self.n):

                if self.matrix[x][v] == 1 or self.matrix[v][x] == 1:
                    if x not in visited:
                        stack.append(x)

                if len(visited) == self.n:
                    connected = True

            visited.add(v)

        return connected

    def find_a_mother_node(self):


        for x in range(self.n):

            visited = {x}
            stack = [x]
            seen = {x}

            while stack:
                v = stack.pop()

                for next_v in range(self.n):
                    if self.matrix[v][next_v] == 1:
                        if next_v not in visited:
                            stack.append(next_v)

                        seen.add(next_v)
                visited.add(v)
                if len(seen) == self.n:
                    return x
        else:
            return None


    def find_mother2(self):
        # DFS backwards to find all potential mothers
        # then check if it's a mother

        pass





if __name__ == '__main__':

    graph = Graph(0.35, 5)
    print(graph)
    print(graph.is_connected())

    print(graph.find_a_mother_node())


