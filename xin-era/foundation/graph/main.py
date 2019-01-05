import random
import pickle


class Graph:

    def load(self, path):
       with open(path, 'rb') as file:
           pickled = pickle.load(file)
           self.graph = pickled.graph
           self.bidirectional = pickled.bidirectional

    def save(self, path):
        with open(path, 'wb') as file:
            pickle.dump(self, file)

    def __init__(self, bidirectional=True):
        self.graph = {}
        self.bidirectional = bidirectional


    def vertices(self):
        return self.graph.keys()

    def add_vertex(self, *vertex):
        for v in vertex:
            if v not in self.graph:
                self.graph[v] = set()

    def add_edge(self, source, sink):
        if source == sink:
            return
        if source in self.graph and sink in self.graph:
            self.graph[source].add(sink)
            if self.bidirectional:
                self.graph[sink].add(source)

    def assign_random_edges(self, p):
        if self.bidirectional:
            p /= 2

        for x in self.graph:
            for y in self.graph:
                if random.random() < p:
                    self.add_edge(x, y)

    def __str__(self):
        str = ''
        for x in self.graph:

            str += '\n{} {}'.format(x, self.graph[x] or '_')
        return str

if __name__ == '__main__':
    generate = False

    graph = Graph()
    if generate:
        graph.add_vertex('a', 'b', 'c', 'd', 'e', 'f')
        graph.assign_random_edges(0.5)
        graph.save('saved_graph.pickle')
    else:
        graph.load('saved_graph.pickle')

    print(graph)


