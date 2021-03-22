# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
  def __init__(self, key, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

    self.root = self.__createTree(0)
    self.inOrderResult = []
    self.preOrderResult = []
    self.postOrderResult = []
  
  def __createTree(self, i):
    if i < self.n:
      if self.right[i] == -1:
        if self.left[i] == -1:
          return Node(self.key[i], left=None, right=None)
        else:
          return Node(self.key[i], left=self.__createTree(self.left[i]), right=None)
      else:
        if self.left[i] == -1:
          return Node(self.key[i], left=None, right=self.__createTree(self.right[i]))
        else:
          return Node(self.key[i], left=self.__createTree(self.left[i]), right=self.__createTree(self.right[i]))
  
  def __inOrder(self, node):
    if node != None:
      self.__inOrder(node.left)
      self.inOrderResult.append(node.key)
      self.__inOrder(node.right)

  def inOrder(self):
    # Left, Root, Right
    self.__inOrder(self.root)        
    return self.inOrderResult
  
  def __preOrder(self, node):
    if node != None:
      self.preOrderResult.append(node.key)
      self.__preOrder(node.left)
      self.__preOrder(node.right)

  def preOrder(self):
    # Root, Left, Right
    self.__preOrder(self.root)         
    return self.preOrderResult

  def __postOrder(self, node):
    if node != None:
      self.__postOrder(node.left)
      self.__postOrder(node.right)
      self.postOrderResult.append(node.key)

  def postOrder(self):
    # Left, Right, Root
    self.__postOrder(self.root)           
    return self.postOrderResult

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
