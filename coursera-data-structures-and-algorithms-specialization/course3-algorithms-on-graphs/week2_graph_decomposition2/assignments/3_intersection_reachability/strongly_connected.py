#Uses python3

import sys

sys.setrecursionlimit(200000)

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
    
    def explore(self, v, li):
        v.visited = True
        self.previsit(v)
        for w in v.adj:
            if not w.visited:
                li.append(w)
                self.explore(w, li)
        self.postvisit(v)   
    
    def DFS(self):
        for v in self.vertices:
            if not v.visited:
                self.explore(v, [v])
    
    def postvisit(self, v):
        v.post = self.clock
        self.clock += 1
    
    def previsit(self, v):
        v.pre = self.clock
        self.clock += 1
    
    def topological_sort(self):
        self.DFS()
        vertices = sorted(self.vertices, key=lambda v: v.post, reverse=True)
        vertices = [v.key for v in vertices]
        return vertices
    
    def strongly_connected_components(self, order):
        self.change_order(order)
        gcc_list = []
        for v in self.vertices:
            if not v.visited:
                gcc = [v]
                self.explore(v,gcc)
                gcc_list.append(gcc)
        return gcc_list
    
    def change_order(self, order):
        new = []
        for i in order:
            new.append(self.vertices[i])
        self.vertices = new
        
def reverse_edges(adj):
    reverse = [[] for _ in range(len(adj))]
    for i, l in enumerate(adj):
        for x in l:
            reverse[x].append(i)
    return reverse

def number_of_strongly_connected_components(adj, n):
    #write your code here
    adj_reversed = reverse_edges(adj)
    graph = Graph(adj, n)
    graph_reversed = Graph(adj_reversed, n)
    topo_order = graph_reversed.topological_sort()
    gcc_list = graph.strongly_connected_components(topo_order)
    return len(gcc_list)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj,n))
