#Uses python3

import sys
import queue


class Vertex:
    def __init__(self, key):
        self.key = key
        self.adj = []
        self.visited = False

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
        dist, prev = dict(), dict()
        for u in self.vertices:
            dist[u] = -1
            prev[u] = None
        dist[s] = 0
        q = queue.Queue(maxsize=n)
        q.put(s)
        while not q.empty():
            u = q.get()
            for v in u.adj:
                if dist[v] == -1:
                    q.put(v)
                    dist[v] = dist[u] + 1
                    prev[v] = u
        return prev, dist
    
    def reconstruct_path(self, s, u, prev):
        result = []
        while t != s:
            result.append(u)
            try:
                t = prev[t]
            except KeyError:
                return []
        return list(reversed(result))

def distance(adj, n, s, t):
    #write your code here
    graph = Graph(adj, n)
    s = graph.vertices[s]
    t = graph.vertices[t]
    prev, dist = graph.BFS(s)
    return dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, n, s, t))
