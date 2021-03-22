# python3
import sys

class SuffixTree:
	class Vertex:
		def __init__(self, label):
			self.label = label
			self.edges = dict()
	
	def __init__(self, text):
		""" Make suffix tree, without suffix links, 
		from s in quadratic time and linear space """
		self.root = self.Vertex(None)
		self.root.edges[text[0]] = self.Vertex(text) # trie for just longest suffix
        # Add rest suffixes, from longest to shortest
		for i in range(1, len(text)):
            # start at root; we’ll walk down as far as we can go
			cur_node = self.root
			j = i
			while j < len(text):
				if text[j] in cur_node.edges:
					child = cur_node.edges[text[j]]
					label = child.label
                    # Walk along edge until we exhaust edge label or
                    # until we mismatch
					k = j+1 
					while k-j < len(label) and text[k] == label[k-j]:
						k += 1
					if k-j == len(label):
						cur_node = child # we exhausted the edge
						j = k
					else:
                        # we fell off in middle of edge
						cExist, cNew = label[k-j], text[k]
                        # create “mid”: new node bisecting edge
						mid = self.Vertex(label[:k-j])
						mid.edges[cNew] = self.Vertex(text[k:])
                        # original child becomes mid’s child
						mid.edges[cExist] = child
                        # original child’s label is curtailed
						child.label = label[k-j:]
                        # mid becomes new child of original parent
						cur_node.edges[text[j]] = mid
				else:
					# Fell off tree at a node: make new edge hanging off it
					cur_node.edges[text[j]] = self.Vertex(text[j:])

	def traverse(self):
		current = self.root
		stack, res = [], []
		while True:
			if bool(current.edges):
				k = list(current.edges.keys())[0]
				stack.append(current.edges[k])
				del current.edges[k]
			elif stack:
				current = stack.pop()
				res.append(current.label)
			else:
				break
		return res

def build_suffix_tree(text):
	"""
	Build a suffix tree of the string text and return a list
	with all of the labels of its edges (the corresponding 
	substrings of the text) in any order.
	"""
	# Implement this function yourself
	tree = SuffixTree(text)
	result = tree.traverse()
	return result

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))