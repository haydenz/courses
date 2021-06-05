# python3
import queue


class Edge:
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

    def check(self):
        return self.capacity - self.flow

class FlowGraph:
    def __init__(self, n):
        self.edges = []
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    n, m = map(int, input().split()) # n = the number of flights, m = the number of crews
    graph = FlowGraph(m+n+2)
    for i in range(n):
        graph.add_edge(-1, i, 1)
        onehot = input().split()
        for j in range(len(onehot)):
            if int(onehot[j]) == 1:
                graph.add_edge(i, n+j, 1)
    for i in range(m):
        graph.add_edge(n+i, n+m, 1)
    return graph, n, m


def bfs(graph, from_, to):
    q = queue.Queue()
    q.put((from_, []))

    visited = set()
    while not q.empty():
        (u, p) = q.get()
        if u in visited:
            continue
        visited.add(u)
        edges = graph.get_ids(u)
        for e in edges:
            edge = graph.get_edge(e)
            if edge.v in visited:
                continue
            if edge.check() > 0:
                if edge.v == to:
                    p.append(e)
                    return p
                next = list(p)
                next.append(e)
                q.put((edge.v, next))

    return None


def max_flow(graph, from_, to):
    flow = 0
    while True:
        p = bfs(graph, from_, to)
        if p is None:
            break
        _min = graph.get_edge(p[0]).check()
        for e in p:
            tmp = graph.get_edge(e).check()
            if tmp < _min:
                _min = tmp
        for e in p:
            graph.add_flow(e, _min)
        flow += _min
    return graph

class MaxMatching:
    def _read_data(self):
        return read_data()

    def _max_flow(self, graph, from_, to):
        return max_flow(graph, from_, to)

    def _find_matching(self, graph, n, m):
        res = ['-1' for _ in range(n)]
        for i in range(n):
            for j in graph.get_ids(i):
                edge = graph.get_edge(j)
                if edge.flow != 1 or edge.v < n:
                    continue
                res[i] = str(edge.v + 1 - n)
                break
        print(' '.join(res))


    def solve(self):
        graph, n, m = self._read_data()
        graph = self._max_flow(graph, -1, n+m)
        self._find_matching(graph, n, m)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
