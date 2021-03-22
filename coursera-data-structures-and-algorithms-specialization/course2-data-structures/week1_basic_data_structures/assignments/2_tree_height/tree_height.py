# python3

import sys
import threading

# TODO: simplify by assigning a level to each node while doing the breadth-wise search

class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

    def addChild(self, theChild):
        self.children.append(theChild)
    
    def getSize(self):
        return len(self.children)

def compute_height(n, parents):
    # Replace this code with a faster implementation

    nodes = []
    for i in range(n):
        nodes.append(Node(i))
    
    for child_idx in range(n):
        parent_idx = parents[child_idx]
        if parent_idx == -1:
            root = child_idx
        else:
            nodes[parent_idx].addChild(nodes[child_idx])
    
    q = [nodes[root]]
    height = 1
    curr_num = 1
    next_num = 0
    i = 0
    count = 0
    while len(q) != 0:
        node = q[0]
        i += 1
        count += 1
        if node == 'Hello':
            # print(node)
            height += 1
            q.pop(0)
            if len(q) == 0:
                break
            else:
                node = q[0]
                q.pop(0)
                # print(node.key)
        else:
            if len(q) == 0:
                break
            else:
                q.pop(0)
                # print(node.key)
        
        if i < curr_num:
            next_num += node.getSize()
            q += node.children
        elif i == curr_num:
            next_num += node.getSize()
            i = 0
            curr_num = next_num
            next_num = 0
            q += node.children
            if count < n:
                q.append('Hello')
        
                    

    return height

    '''
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height
    '''


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    # n = 10
    # parents = [8, 8, 5, 6, 7 ,3, 1, 6, -1, 5]
    print(compute_height(n, parents))

# 
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

# if __name__ == '__main__':
    # # main()
