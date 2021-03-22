#Uses python3

import sys

class Vertex:
    def __init__(self, x):
        self.key = x
        self.adj = []
        self.visited = False
        self.pre = 0
        self.post = 0

def reach(vertices, x, y):
    explore(vertices[x])
    return '1' if nested(vertices[x], vertices[y]) else '0'

def explore(v):
    v.visited = True
    previsit(v)
    for w in v.adj:
        if not w.visited:
            explore(w)
    postvisit(v)

clock = 1
def previsit(v):
    global clock
    v.pre = clock
    clock += 1

def postvisit(v):
    global clock
    v.post = clock
    clock += 1

def nested(x, y):
    return (x.pre < y.pre and x.post > y.post) or (y.pre < x.pre and y.post > x.post)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    vertices = [None for i in range(n)]
    for i in range(n):
        vertices[i] = Vertex(i)
    for i in range(n):
        for a in adj[i]:
            vertices[i].adj.append(vertices[a])
    print(reach(vertices, x, y))
