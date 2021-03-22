#Uses python3

import sys


class Vertex:
    def __init__(self, x):
        self.key = x
        self.adj = []
        self.visited = False
        self.stack = False
        self.post = 0
        self.pre = 0

class Graph:
    def __init__(self, adj, n):
        self.adj = adj
        self.n = n
        self.vertices = self.create_graph(self.adj)
        self.clock = 1

    def create_graph(self, adj):
        vertices = [None for i in range(n)]
        for i in range(self.n):
            vertices[i] = Vertex(i)
        for i in range(n):
            for a in adj[i]:
                vertices[i].adj.append(vertices[a])
        return vertices
    
    def explore(self, v):
        # Mark current node as visited
        v.visited = True
        # Add to recursion stack
        v.stack = True
        # For all neighbors of current node, 
        # if any neighbor is visited and in the
        # recursion stack, then the graph contains circle
        self.previsit(v)
        for w in v.adj:
            if not w.visited:
                if self.explore(w):
                    return True
            elif w.stack:
                return True
        self.postvisit(v)
        v.stack = False
        return False     
    
    def FDS(self):
        for v in self.vertices:
            if not v.visited:
                if self.explore(v):
                    return True
        return False
    
    def postvisit(self, v):
        v.post = self.clock
        self.clock += 1
    
    def previsit(self, v):
        v.pre = self.clock
        self.clock += 1
    
    def topological_sort(self):
        is_cyclic = self.FDS()
        # TODO: add info output when the graph contains circles
        # if not is_cyclic: 
        vertices = sorted(self.vertices, key=lambda v: v.post, reverse=True)
        vertices = [v.key for v in vertices]
        return vertices

def toposort(adj, n):
    used = [0] * len(adj)
    order = []
    #write your code here
    directed_graph = Graph(adj, n)
    return directed_graph.topological_sort()

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj, n)
    for x in order:
        print(x + 1, end=' ')
