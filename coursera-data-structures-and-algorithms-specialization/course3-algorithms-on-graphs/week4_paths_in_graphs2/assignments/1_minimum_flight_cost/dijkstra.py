#Uses python3

import sys
import queue
import random as rd

 
class Heap():
    def __init__(self, data):
        self.array, self.pos = self.create_array(data)
        self.size = len(self.array)
 
    def create_array(self, data):
        arr, pos = [], []
        for i, d in enumerate(data):
            pos.append(i)
            arr.append(d)
        return arr, pos
 
    def swap_node(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]
 
    def heapify(self, idx): # raise up minimum node
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2
        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left
        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right
        if smallest != idx:
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest
            self.swap_node(smallest, idx)
            self.heapify(smallest)
 
    def extract_min(self):
        if self.is_empty() == True:
            return
        root = self.array[0]
        last_node = self.array[self.size - 1]
        self.array[0] = last_node
        self.pos[last_node[0]] = 0
        self.pos[root[0]] = self.size - 1
        self.size -= 1
        self.heapify(0)
        return root
 
    def is_empty(self):
        return True if self.size == 0 else False
 
    def decrease_key(self, v, dist):
        i = self.pos[v]
        self.array[i][1] = dist
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i
            self.swap_node(i, (i - 1)//2 )
            i = (i - 1) // 2;
 
    def in_heap(self, v):
        if self.pos[v] < self.size:
            return True
        return False

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
    
    def create_vertices(self):
        vertices = [None for _ in range(self.n)]
        for i in range(self.n):
            vertices[i] = Vertex(i)
        for i in range(self.n):
            vertices[i].cost = self.cost[i]
            for a in adj[i]:
                vertices[i].adj.append(vertices[a])
        self.vertices = vertices
    
    def dijkstra(self, s):
        dist, prev = dict(), dict()
        for u in self.vertices:
            dist[u], prev[u] = sys.maxsize, None
        dist[s] = 0

        heap_l = [[u.key, dist[u]] for u in self.vertices]
        h = Heap(heap_l)        
        h.decrease_key(s.key, dist[s])

        while not h.is_empty():
            u = self.vertices[h.extract_min()[0]]
            for v in u.adj:
                if v == u:
                    continue
                v_dist_old = dist[v]
                v_adj_idx = u.adj.index(v)
                tmp = dist[u] + u.cost[v_adj_idx]
                if dist[v] > tmp and dist[u] != sys.maxsize and h.in_heap(v.key):
                    dist[v] = tmp
                    prev[v] = u
                    h.decrease_key(v.key, dist[v])
        return dist

def distance(adj, cost, s, t):
    #write your code here
    if (s not in range(len(adj))) or (t not in range(len(adj))):
        return -1
    graph = Graph(adj, cost)
    vertices = graph.vertices
    dist = graph.dijkstra(vertices[s])
    tmp = dist[vertices[t]]
    return tmp if tmp != sys.maxsize else -1

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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
