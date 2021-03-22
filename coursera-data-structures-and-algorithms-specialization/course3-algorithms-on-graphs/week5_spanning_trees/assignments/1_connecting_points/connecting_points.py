#Uses python3
import sys
import math

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
    def __init__(self, key, x, y):
        self.key = key
        self.adj = []
        self.cost = []
        self.visited = False
        self.x = x
        self.y = y

class Graph:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.vertices = []
        self.edges = []
        self.create_vertices()
    
    def distance(self, a, b):
        _x = pow(a.x - b.x, 2)
        _y = pow(a.y - b.y, 2)
        return math.sqrt(_x + _y)

    def create_vertices(self):
        vertices = [None for _ in range(self.n)]
        for i in range(self.n):
            vertices[i] = Vertex(i, self.x[i], self.y[i])
        for i in range(self.n):
            for j in range(i, self.n):
                if i != j:
                    cost = self.distance(vertices[i], vertices[j])
                    vertices[i].cost.append(cost)
                    vertices[j].cost.append(cost)

                    vertices[i].adj.append(vertices[j])
                    vertices[j].adj.append(vertices[i])

                    self.edges.append((vertices[i], vertices[j]))
                    self.edges.append((vertices[j], vertices[i]))
        self.vertices = vertices
    
    def prim(self):
        s = self.vertices[0]
        cost, parent = dict(), dict()
        for u in self.vertices:
            cost[u.key], parent[u.key] = math.inf, None
        cost[s.key] = 0

        heap_l = [[u.key, cost[u.key]] for u in self.vertices]
        h = Heap(heap_l)        
        h.decrease_key(s.key, cost[s.key])

        while not h.is_empty():
            u = self.vertices[h.extract_min()[0]]
            for v in u.adj:
                v_adj_idx = u.adj.index(v)
                tmp = u.cost[v_adj_idx]
                if cost[v.key] > tmp and h.in_heap(v.key):
                    cost[v.key] = tmp
                    parent[v.key] = [u.key, tmp]
                    h.decrease_key(v.key, cost[v.key])
        return parent

def minimum_distance(x, y):
    #write your code here
    g = Graph(x, y)
    vertices = g.vertices
    parent = g.prim()

    res = 0
    for child in parent:
        if parent[child] is not None:
            res += parent[child][1]

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
