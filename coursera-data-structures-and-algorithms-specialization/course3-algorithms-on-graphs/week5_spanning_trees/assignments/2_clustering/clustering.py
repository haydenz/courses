#Uses python3
import sys
import math

class Heap():
    def __init__(self, data):
        self.array, self.pos = self.create_array(data)
        self.size = len(self.array)
 
    def create_array(self, data):
        arr, pos = [], []
        for i, (edge, cost) in enumerate(data):
            pos.append(i)
            arr.append((i, edge, cost))
        return arr, pos
    
    def sort(self):
        for i in range(self.size//2, -1, -1):
            self.heapify(i)
 
    def swap_node(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]
 
    def heapify(self, idx): # raise up minimum node
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2
        if left < self.size and self.array[left][2] < self.array[smallest][2]:
            smallest = left
        if right < self.size and self.array[right][2] < self.array[smallest][2]:
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
        self.array[i][2] = dist
        while i > 0 and self.array[i][2] < self.array[(i - 1) // 2][2]:
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i
            self.swap_node(i, (i - 1)//2 )
            i = (i - 1) // 2;
 
    def in_heap(self, v):
        if self.pos[v] < self.size:
            return True
        return False

class DisjointTrees:
    def __init__(self, points):
        self.points = points
        self.num = len(points)
        self.rank = [1 for _ in range(self.num)]
        self.parent = [i for i in range(self.num)]
        self.cluster_num = self.num
    
    def find(self, idx):
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]
    
    def union(self, i, j):
        i_parent = self.find(i)
        j_parent = self.find(j)
        if i_parent == j_parent:
            return
        
        if self.rank[i_parent] > self.rank[j_parent]:
            self.parent[j_parent] = i_parent
        else:
            self.parent[i_parent] = j_parent
            if self.rank[i_parent] == self.rank[j_parent]:
                self.rank[j_parent] += 1
        self.cluster_num -= 1
    

class Vertex:
    def __init__(self, key, x, y):
        self.key = key
        self.adj = []
        # self.cost = []
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
                    # vertices[i].cost.append(cost)
                    # vertices[j].cost.append(cost)

                    vertices[i].adj.append(vertices[j])
                    vertices[j].adj.append(vertices[i])

                    self.edges.append([(i, j), cost])
                    self.edges.append([(j, i), cost])
        self.vertices = vertices
    
    def kruskal(self, k):
        trees = DisjointTrees(self.vertices)
        # sort edges by cost
        h = Heap(self.edges)
        h.sort()
        x = []
        while trees.cluster_num >= k:
            i, (u,v), cost = h.extract_min()
            if trees.find(u) != trees.find(v):
                x.append((u,v))
            trees.union(u,v)
        return cost


def clustering(x, y, k):
    #write your code here
    g = Graph(x,y)
    return g.kruskal(k)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.12f}".format(clustering(x, y, k)))
