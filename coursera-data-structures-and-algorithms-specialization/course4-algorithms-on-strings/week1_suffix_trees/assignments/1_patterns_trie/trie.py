#Uses python3
import sys

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = dict() # {edge: EndVertex.label}

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    label = 0
    root = Vertex(label)
    for pattern in patterns:
        curr_node = root
        for i in range(len(pattern)):
            curr_symbol = pattern[i]
            if bool(curr_node.edges) and curr_symbol in curr_node.edges:
                curr_node = Vertex(curr_node.edges[curr_symbol])
                curr_node.edges = tree[curr_node.label]   
            else:
                label += 1
                new_node = Vertex(label)
                curr_node.edges.update({curr_symbol: new_node.label})
                tree.update({curr_node.label: curr_node.edges})
                curr_node = new_node
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    # patterns = ["ATAGA", "ATC", "GAT"]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
