#Uses python3

import sys

class Vertex:
    def __init__(self, key):
        self.key = key
        self.adj = []
        self.cost = []
        self.visited = False

class Graph:
    def __init__(self, adj, cost):
        self.adj = adj
        self.n = len(adj)
        self.cost = cost
        self.vertices = []
        self.create_vertices()
        self.edges = self.edges()
    
    def create_vertices(self):
        vertices = [None for _ in range(self.n)]
        for i in range(self.n):
            vertices[i] = Vertex(i)
        for i in range(self.n):
            vertices[i].cost = self.cost[i]
            for a in adj[i]:
                vertices[i].adj.append(vertices[a])
        self.vertices = vertices
    
    def edges(self):
        res = []
        for u in self.vertices:
            for v in u.adj:
                res.append((u, v))
        return res

    def bellman_ford(self):
        s = self.vertices[0]
        dist, prev = dict(), dict()
        for u in self.vertices:
            dist[u], prev[u] = sys.maxsize, None
        dist[s] = 0
        flag = False

        for i in range(self.n):
            for (u, v) in self.edges:
                f = self.relax(u, v, dist, prev)
                if i == self.n-1:
                    if f:
                        flag = True
        return flag

    def relax(self, u, v, dist, prev):
        flag = False
        v_adj_idx = u.adj.index(v)
        tmp = dist[u] + u.cost[v_adj_idx]
        if dist[v] > tmp:
            dist[v] = tmp
            prev[v] = u
            flag = True
        del tmp
        return flag

def negative_cycle(adj, cost):
    #write your code here
    graph = Graph(adj, cost)
    return 1 if graph.bellman_ford() else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
