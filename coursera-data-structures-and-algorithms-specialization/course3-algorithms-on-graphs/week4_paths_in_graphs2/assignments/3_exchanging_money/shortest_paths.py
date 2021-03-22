#Uses python3

import sys
import math

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
        self.edges = []
        self.create_vertices()
    
    def create_vertices(self):
        vertices = [None for _ in range(self.n)]
        for i in range(self.n):
            vertices[i] = Vertex(i)
        for i in range(self.n):
            vertices[i].cost = self.cost[i]
            for a in adj[i]:
                vertices[i].adj.append(vertices[a])
                self.edges.append((vertices[i], vertices[a]))
        self.vertices = vertices

    def bellmanford(self, s):
        global distance, reachable, shortest
        dist, prev = dict(), dict()
        for u in self.vertices:
            dist[u.key], prev[u.key] = math.inf, None
        dist[s.key] = 0
        distance[s.key] = 0
        reachable[s.key] = 1
        flag = False
        found = []
        for i in range(self.n):
            for (u, v) in self.edges:
                f = self.relax(u, v, dist, prev, last=i==self.n-1)
                if i == self.n - 1 and f:
                    flag = True
                    found.append(v.key)
        return flag, found, dist

    def relax(self, u, v, dist, prev, last=True):
        global distance, reachable, shortest
        flag = False
        v_adj_idx = u.adj.index(v)
        tmp = dist[u.key] + u.cost[v_adj_idx]
        if dist[v.key] > tmp:
            if last:
                flag = True
            else:
                dist[v.key] = tmp
                prev[v.key] = u.key
                distance[v.key] = tmp
                reachable[v.key] = 1 if tmp != math.inf else 0
        del tmp
        return flag

def shortest_paths(adj, cost, s):
    global distance, reachable, shortest
    #write your code here
    g = Graph(adj, cost)
    vertices = g.vertices
    source = vertices[s]
    flag, found, dist = g.bellmanford(source)

    if flag:
        # Create a queue q
        q = []
        for n in found:
            q.append(n)
        # BFS: all nodes reachable form the negative cycles
        while len(q) != 0:
            u = vertices[q[0]]
            q = q[1:]
            if not u.visited:
                u.visited = True
                if dist[u.key] == math.inf:
                    reachable[u.key] = 0 #TODO
                shortest[u.key] = 0
                for v in u.adj:
                    if not v.visited and v.key not in q:
                        q.append(v.key)

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
    s = data[0]
    s -= 1
    distance = [math.inf] * n
    reachable = [0] * n
    shortest = [1] * n

    shortest_paths(adj, cost, s)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
