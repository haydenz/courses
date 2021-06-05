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

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
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
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split()) # integers n,m: number of cities and number of roads
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


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
    return flow

if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
