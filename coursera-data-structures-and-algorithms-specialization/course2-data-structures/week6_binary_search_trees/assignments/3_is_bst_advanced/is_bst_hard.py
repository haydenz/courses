#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def InOrderLeft(tree, idx, min_key, max_key): 
  if idx < len(tree):
    left = tree[idx][1]
    right = tree[idx][2]
    key = tree[idx][0]
  
    if key <= min_key or key >= max_key:
      return False
    
    if left != -1 and right != -1:
      return InOrderLeft(tree, left, min_key, max_key=key) and InOrderRight(tree, right, key, max_key)
    elif left != -1 and right == -1:
      return InOrderLeft(tree, left, min_key, max_key=key)
    elif left == -1 and right != -1:
      return InOrderRight(tree, right, key, max_key)
    else:
      return True

def InOrderRight(tree, idx, min_key, max_key):
  if idx < len(tree):
    left = tree[idx][1]
    right = tree[idx][2]
    key = tree[idx][0]

    if key < min_key or key > max_key:
      return False

    if left != -1 and right != -1:
      return InOrderLeft(tree, left, min_key-1, max_key=key) and InOrderRight(tree, right, key, max_key)
    elif left != -1 and right == -1:
      return InOrderLeft(tree, left, min_key-1, max_key=key)
    elif left == -1 and right != -1:
      return InOrderRight(tree, right, key, max_key)
    else:
      return True

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if not tree:
    return True
  lower = - 2**31
  upper = 3**31 - 1

  if tree[0][1] != -1 and tree[0][2] != -1:
    return InOrderLeft(tree, tree[0][1], min_key=lower-1, max_key=tree[0][0]) and InOrderRight(tree, tree[0][2], min_key=tree[0][0], max_key=upper)
  elif tree[0][1] != -1 and tree[0][2] == -1:
    return InOrderLeft(tree, tree[0][1], min_key=lower-1, max_key=tree[0][0])
  elif tree[0][1] == -1 and tree[0][2] != -1:
    return InOrderRight(tree, tree[0][2], min_key=tree[0][0], max_key=upper)
  else:
    return tree[0][0] >= lower and tree[0][0] <= upper

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
