# python3
import sys

SYMBOL1 = "#"
SYMBOL2 = "$"

class SuffixTree:
	class Vertex:
		def __init__(self, label):
			self.label = label
			self.edges = dict()
			self.text1 = False
			self.pos = None
	
	def __init__(self, text, len_p):
		""" Make suffix tree, without suffix links, 
		from s in quadratic time and linear space """
		self.root = self.Vertex(None)
		self.root.pos = (0, 0, len(text))
		self.text = text
		self.len_p = len_p
		all_text = self.Vertex(text)
		all_text.pos = (0, 0, len(text))
		if len_p != 0:
			all_text.text1 = True
		self.root.edges[text[0]] =  all_text# trie for just longest suffix
        # Add rest suffixes, from longest to shortest
		for i in range(1, len(text)):
            # start at root; we’ll walk down as far as we can go
			cur_node = self.root
			j = i
			while j < len(text):
				if text[j] in cur_node.edges:
					child = cur_node.edges[text[j]]
					label = child.label
					# if not child.text1:
					child.text1 = True if j <= len_p else False
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
						mid.pos = (child.pos[0], child.pos[1], len(label[:k-j])) #mid.text1 = True if child.pos[1] <= len_p else False
					
						tmp = self.Vertex(text[k:])
						tmp.pos = (i, k, len(text[k:]))
						tmp.text1 = True if k <= len_p else False
						
						mid.edges[cNew] = tmp
						# original child becomes mid’s child
						
                        # original child’s label is curtailed
						child.label = label[k-j:]
						child.pos = (child.pos[0], child.pos[1]+k-j, len(label[k-j:]))
						if bool(child.edges):
							child.text1 = all([(child.edges[n]).text1 for n in child.edges])
						else:
							child.text1 = True if child.pos[1] <= len_p else False
						mid.edges[cExist] = child
						
						if bool(mid.edges):
							mid.text1 = all([(mid.edges[n]).text1 for n in mid.edges])
						else:
							mid.text1 = True if mid.pos[1] <= len_p else False
						cur_node.edges[text[j]] = mid
						cur_node.text1 = all([(cur_node.edges[n]).text1 for n in cur_node.edges])
				else:
					# Fell off tree at a node: make new edge hanging off it
					new_node = self.Vertex(text[j:])
					new_node.pos = (i, j, len(text[j:]))
					new_node.text1 = True if j <= len_p else False
					# cur_node.text1 = all([(cur_node.edges[n]).text1 for n in cur_node.edges])
					cur_node.edges[text[j]] = new_node

	def mark_text1(self, node):
		node.text1 = True
		res = True
		if node.pos[1] > self.len_p:
			node.text1 = False
			res = False

		for k in node.edges:
			child = node.edges[k]
			res_tmp = self.mark_text1(child)
			child.text1 = res_tmp
			if res_tmp == False:
				res = False
		
		node.text1 = res
		return res

	def max_label(self):
		current = self.root
		# self.mark_text1(current)
		stack, res = [], []
		while True:
			if bool(current.edges):
				k = list(current.edges.keys())[0]
				if bool(current.edges[k].edges) or current.edges[k].text1:
					stack.append(current.edges[k])
				del current.edges[k]
			elif stack:
				current = stack.pop()
				init, pos, length = current.pos
				if current.text1:
					if current.label[0] == SYMBOL1:
						pass
						# if pos-init > 1:
						# 	res.append(self.text[init:pos])
						# tmp = self.text[init:pos]
						# if tmp != '':
						# 	res.append(tmp)
					else:
						res.append(self.text[init:pos+1])
			else:
				break
		return min(res, key=len)	
	
	def path(self, node):
		pass

def solve(p, q):
	tree = SuffixTree(p+SYMBOL1+q+SYMBOL2, len_p=len(p))
	return tree.max_label()

if __name__ == '__main__':
	p = sys.stdin.readline ().strip ()
	q = sys.stdin.readline ().strip ()
	ans = solve(p, q)
	sys.stdout.write (ans + '\n')
