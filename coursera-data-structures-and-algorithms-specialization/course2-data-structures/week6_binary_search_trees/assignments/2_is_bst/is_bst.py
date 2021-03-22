#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
  def __init__(self, key, parent=None, left=None, right=None):
    self.key = key
    self.parent = parent
    self.left = left
    self.right = right

def createTree(tree_list, i, parent_idx):
  if i < len(tree_list):
    key = tree_list[i][0]
    left = tree_list[i][1]
    right = tree_list[i][2]

    if right == -1:
      if left == -1:
        return Node(key, parent=parent_idx, left=None, right=None)
      else:
        return Node(key, parent=parent_idx, left=createTree(tree_list, left, i), right=None)
    else:
      if left == -1:
        return Node(key, parent=parent_idx, left=None, right=createTree(tree_list, right, i))
      else:
        return Node(key, parent=parent_idx, left=createTree(tree_list, left, i), right=createTree(tree_list, right, i))

def preOrder(node, tree_list, pos=None):
  tmp = 1
  if node != None:
    parent = tree_list[node.parent][0]
    if node.left != None:
      if (node.key <= node.left.key) or (pos == 'right' and node.left.key <= parent):
        return 0
    if node.right != None:
      if (node.key >= node.right.key) or (pos == 'left' and node.right.key >= parent):
        return 0
    tmp *= preOrder(node.left, tree_list, pos='left')
    tmp *= preOrder(node.right, tree_list, pos='right')
  return tmp

def IsBinarySearchTree(root, tree_list):
  # Implement correct algorithm here
  if preOrder(root, tree_list) == 1:
    return True
  return False

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  root = createTree(tree, 0, 0)
  if IsBinarySearchTree(root, tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
