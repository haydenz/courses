# python3
import sys

NA = -1
class Vertex:
	def __init__(self, label):
		self.pattern_end = False
		self.label = label
		self.edges = dict()

def build_trie(patterns):
	tree, label = dict(), 0
	root = Vertex(label)
	for pattern in patterns:
		curr_node = root
		pattern_end = False
		for i in range(len(pattern)):
			curr_symbol = pattern[i]
			if i == len(pattern) - 1:
				pattern_end = True
			try:
				if tree[curr_node.label][curr_symbol].pattern_end:
					pattern_end = True
			except Exception as e:
				pass

			if bool(curr_node.edges) and curr_symbol in curr_node.edges:
				curr_node = curr_node.edges[curr_symbol]
				curr_node.pattern_end = pattern_end
			else:
				label += 1
				new_node = Vertex(label)
				new_node.pattern_end = pattern_end
				curr_node.edges.update({curr_symbol: new_node})
				tree.update({curr_node.label: curr_node.edges})
				curr_node = new_node
	return root

def prefix_trie_matching(text, trie):
	pos, l, flag = 0, [], False
	symbol = text[pos]
	v = trie
	while True:
		if not bool(v.edges):
			return flag, l
		elif symbol in v.edges:
			if v.pattern_end:
				flag = True
			l.append(symbol)
			pos += 1
			v = v.edges[symbol]
			if v.pattern_end:
				flag = True
			try:
				symbol = text[pos]
			except IndexError:
				return flag, l
		else:
			return flag, l

def trie_matching(text, trie):
	count, res, all_l = 0, [], []
	while len(text) > 0:
		matched, l = prefix_trie_matching(text, trie)
		if matched:
			res.append(count)
		text = text[1:]
		count += 1
		all_l.append(l)
	return res

def solve (text, n, patterns):
	result = []
	# write your code here
	trie = build_trie(patterns)
	result = trie_matching(text, trie)
	return result

if __name__ == "__main__":
	text = sys.stdin.readline ().strip ()
	n = int (sys.stdin.readline ().strip ())
	patterns = []
	for i in range (n):
		patterns += [sys.stdin.readline ().strip ()]

	ans = solve (text, n, patterns)

	sys.stdout.write (' '.join (map (str, ans)) + '\n')
