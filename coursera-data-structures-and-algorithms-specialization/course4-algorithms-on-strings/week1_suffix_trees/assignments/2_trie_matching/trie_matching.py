# python3
import sys

NA = -1

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = dict() # {edge: EndVertex.label}

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

def prefix_trie_matching(text, trie):
	pos, l = 0, []
	symbol = text[pos]
	v = Vertex(0)
	v.edges = trie[0]
	while True:
		if not bool(v.edges):
			return True
		elif symbol in v.edges:
			next_node = v.edges[symbol]
			v = Vertex(next_node)
			try:
				v.edges = trie[next_node]
			except Exception as e:
				pass
			pos += 1
			try:
				symbol = text[pos]
			except IndexError:
				if not bool(v.edges):
					return True
				else:
					return False
		else:
			# print("no matches found")
			return False

def trie_matching(text, trie):
	count, res = 0, []
	while len(text) > 0:
		matched = prefix_trie_matching(text, trie)
		if matched:
			res.append(count)
		text = text[1:]
		count += 1
	return res


def solve (text, n, patterns):
	result = []
	# write your code here
	trie = build_trie(patterns)
	result = trie_matching(text, trie)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
