# python3
# Ordered Splay Tree
import sys
from copy import deepcopy

root = None
class Rope:
	def __init__(self, s):
		self.s = s
		for i, char in enumerate(s):
			insert(char, i+1)

	def __inOrderTraverse(self, node):
		# non-recursive version
		current = node
		stack = []
		res = []
		while True:
			if current is not None:
				stack.append(current)
				current = current.left
			elif(stack):
				current = stack.pop()
				res.append(current.key)
				current = current.right
			else:
				break
		return res
	
	def result(self):
		res = self.__inOrderTraverse(root)
		return ''.join(res)

	def process(self, i, j, k):
		global root
        # Write your code here
		(middle, right) = split(root, j + 1)
		if middle != None:
			(left, middle) = split(middle, i)
			remaining = merge(left, right)
			(new_left, new_right) = split(remaining, k)
			root = merge(merge(new_left, middle), new_right)

class Vertex:
	def __init__(self, key, size, left, right, parent):
		(self.key, self.size, self.left, self.right, self.parent) = (key, size, left, right, parent)

def update(v):
	if v == None:
		return
	v.size = 1 + (v.left.size if v.left != None else 0) + (v.right.size if v.right != None else 0)
	if v.left != None:
		v.left.parent = v
	if v.right != None:
		v.right.parent = v

def smallRotation(v):
	parent = v.parent
	if parent == None:
		return
	grandparent = v.parent.parent
	if parent.left == v:
		m = v.right
		v.right = parent
		parent.left = m
	else:
		m = v.left
		v.left = parent
		parent.right = m
	update(parent)
	update(v)
	v.parent = grandparent
	if grandparent != None:
		if grandparent.left == parent:
			grandparent.left = v
		else: 
			grandparent.right = v

def bigRotation(v):
	# Zig-zig
	if v.parent.left == v and v.parent.parent.left == v.parent:
		smallRotation(v.parent)
		smallRotation(v)
	# Zig-zig
	elif v.parent.right == v and v.parent.parent.right == v.parent:
		smallRotation(v.parent)
		smallRotation(v)
	# Zig-zag
	else: 
		smallRotation(v)
		smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
	if v == None:
		return None
	while v.parent != None:
		if v.parent.parent == None:
			smallRotation(v)
			break
		bigRotation(v)
	return v

def order_statistic(root, k):
	# recursive version
	if root != None:
		s = root.left.size if root.left != None else 0
		if k == s + 1:
			return root
		elif k < s + 1:
			return order_statistic(root.left, k)
		else:
			if root.right is not None:
				return order_statistic(root.right, k - s - 1)
			else:
				return None
		root = splay(root)
	else:
		return None

def order_statistic_nonrecursive(node, k):
	if node != None:
		while node:
			s = node.left.size if node.left != None else 0
			if k == s + 1:
				return node
			elif k < s + 1:
				if node.left:
					node = node.left
					continue
				return None
			else:
				if node.right:
					k = k - s - 1
					node = node.right
					continue
				return None
		node = splay(node)
		return node
	else:
		return None

def split(root, k): 
	# result = order_statistic(root, k) 
	result = order_statistic_nonrecursive(root, k)
	
	if result == None:    
		return (root, None)  
	right = splay(result)
	left = right.left
	right.left = None
	if left != None:
		left.parent = None
	update(left)
	update(right)
	return (left, right)
  
def merge(left, right):
	if left == None:
		return right
	if right == None:
		return left
	while right.left != None:
		right = right.left
	right = splay(right)
	right.left = left
	update(right)
	return right

# Code that uses splay tree to solve the problem
                                
def insert(x, k):
	global root
	(left, right) = split(root, k)
	new_vertex = None
	if right == None or right.key != x:
		new_vertex = Vertex(x, 1, None, None, None)
	root = merge(merge(left, new_vertex), right)

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i+1, j+1, k+1)
print(rope.result())
