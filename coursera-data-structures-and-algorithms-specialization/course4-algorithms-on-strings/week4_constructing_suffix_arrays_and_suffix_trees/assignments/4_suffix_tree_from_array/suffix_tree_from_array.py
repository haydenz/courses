# python3
import sys


class Node:
    def __init__(self, id, parent, string_depth, edge_start, edge_end):
        self.id = id
        self.parent = parent
        self.child = []
        self.string_depth = string_depth
        self.edge_start = edge_start
        self.edge_end = edge_end


def break_edge(cur, mid, prev, nodes):
    offset = prev - cur.string_depth
    cur.child[-1] = (mid.id, mid.edge_start, mid.edge_start + offset)
    newleaf = Node(len(nodes), mid, mid.string_depth, mid.edge_start + offset, mid.edge_end)
    newleaf.child = mid.child
    nodes.append(newleaf)
    mid.child = []
    mid.child.append((newleaf.id, newleaf.edge_start, newleaf.edge_end))
    mid.string_depth = cur.string_depth + offset
    mid.edge_end = mid.edge_start + offset

    return mid


def new_leaf(node, s, suffix, nodes):
    start = suffix + node.string_depth
    end = len(s)
    depth = len(s) - suffix
    leaf = Node(len(nodes), node, depth, start, end)
    node.child.append((leaf.id, start, end))
    nodes.append(leaf)

    return leaf


def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label
    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    lt = len(text)
    root = Node(0, None, 0, -1, -1)
    nodes = []
    nodes.append(root)

    prev = 0
    cur = root
    for i in range(lt):
        suffix = sa[i]
        while cur.string_depth > prev:
            visited = cur
            cur= cur.parent
        if cur.string_depth == prev:
            cur = new_leaf(cur, text, suffix, nodes)
        else:
            mid = break_edge(cur, visited, prev, nodes)
            cur = new_leaf(mid, text, suffix, nodes)
        if i < lt - 1:
            prev = lcp[i]

    tree = {}
    for node in nodes:
        id = node.id
        if len(node.child):
            tree[id] = [e for e in node.child]
    return tree


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(sa, lcp, text)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """
    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
      (node, edge_index) = stack[-1]
      stack.pop()
      if not node in tree:
        continue
      edges = tree[node]
      if edge_index + 1 < len(edges):
        stack.append((node, edge_index + 1))
      print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
      stack.append((edges[edge_index][0], 0))
