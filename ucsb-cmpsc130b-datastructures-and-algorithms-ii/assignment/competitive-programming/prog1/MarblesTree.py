'''
https://open.kattis.com/problems/marblestree
'''  
import sys

vertices = {}
# recursively
def count_marbles_recur(node):
    vertices[node][2] = vertices[node][0]
    vertices[node][3] = 1
    # if this node does not have children, then subtree does not have marbles nor vertices
    if not vertices[node][1]:
        pass
    # else, count the marbles of its descendants
    else:
        # marbles_sub, vertices_sub = [sum(x) for x in zip(*[count_marbles_recur(c) for c in vertices[node][1]])]
        tmp = [sum(x) for x in zip(*[count_marbles_recur(c) for c in vertices[node][1]])]
        vertices[node][2] += tmp[0]
        vertices[node][3] += tmp[1]
    return vertices[node][2], vertices[node][3]


def main():
    # take out vertices that has a parent => give us the root of the tree
    tree_root = (set(range(1, n+1)) - set(vertices_has_parents)).pop()
    # count marbles from the root of the tree
    count_marbles_recur(tree_root)
    count = 0
    for m, _, marbles_sub, vertices_sub in vertices.values():
        count += abs(marbles_sub - vertices_sub)
    print(count)

if __name__ == "__main__":
    while True:
        # empty dict
        vertices.clear()
        # number of vertices
        n = int(sys.stdin.readline())
        # exit while loop
        if n == 0:
            break
        vertices_has_parents = []
        for _ in range(n):
            # read each vertex
            i, marble, _, *child = [int(x) for x in sys.stdin.readline().split()]
            vertices[i] = [marble, child, 0, 0]
            vertices_has_parents += child
        main()
