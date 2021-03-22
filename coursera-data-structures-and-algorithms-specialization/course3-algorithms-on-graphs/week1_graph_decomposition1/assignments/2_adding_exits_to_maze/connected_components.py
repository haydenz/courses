#Uses python3

import sys

ConnectedCompNum = 0

class Vertex:
    def __init__(self, x):
        self.key = x
        self.adj = []
        self.visited = False
        self.cc = None

def explore(v):
    global ConnectedCompNum
    v.visited = True
    v.cc = ConnectedCompNum
    for w in v.adj:
        if not w.visited:
            explore(w)

def DFS(vertices):
    global ConnectedCompNum
    for v in vertices:
        if not v.visited:
            explore(v)
            ConnectedCompNum += 1

def number_of_components(vertices):
    #write your code here
    global ConnectedCompNum
    DFS(vertices)
    return ConnectedCompNum

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
    vertices = [None for i in range(n)]
    for i in range(n):
        vertices[i] = Vertex(i)
    for i in range(n):
        for a in adj[i]:
            vertices[i].adj.append(vertices[a])
    print(number_of_components(vertices))
