#Uses python3

import sys
import queue


class Vertex:
    def __init__(self, key):
        self.key = key
        self.adj = []
        self.visited = False
        self.stack = False
        self.color = -1

class Graph:
    def __init__(self, adj, n):
        self.adj = adj
        self.n = n
        self.vertices = []
        self.create_vertices()
    
    def create_vertices(self):
        vertices = [None for _ in range(self.n)]
        for i in range(self.n):
            vertices[i] = Vertex(i)
        for i in range(self.n):
            for a in adj[i]:
                vertices[i].adj.append(vertices[a])
        self.vertices = vertices

    def BFS(self, s):
        flag = True
        s.color = 0
        q = queue.Queue(maxsize=n)
        q.put(s)
        while not q.empty():
            u = q.get()
            if u in u.adj:
                return False
            for v in u.adj:
                if v.color == -1:
                    q.put(v)
                    v.color = 1 - u.color
                elif v.color == u.color:
                    return False
        return True

def bipartite(adj, n):
    #write your code here
    graph = Graph(adj, n)

    for v in graph.vertices:
        if v.color == -1:
            flag = graph.BFS(v)
            if not flag:
                return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    # n,m= 4,2
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # edges = [(1,2),(3,4)]
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    if m != 0:
        print(bipartite(adj, n))
    else:
        print(1)
