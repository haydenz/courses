# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def solve(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans

class CommonSubstring:
	def __init__(self, s, t):
		if len(s) <= len(t):
			self.s = s
			self.t = t
			self.flag = True
		else:
			self.s = t
			self.t = s
			self.flag = False
		self.len_s = len(self.s)
		self.len_t = len(self.t)
		self._prime1 = 1000000007
		self._prime2 = 1000000009
		self._multiplier = 113
		self.poly1 = self.precompute_poly(self.len_t + 1, self._prime1)
		self.poly2 = self.precompute_poly(self.len_t + 1, self._prime2)

	def solve(self):
		if self.s == self.t:
			return Answer(0,0,self.len_s)
		else:
			k = self.len_s
			res = [None for _ in range(k+1)]
			str_l1 = []
			str_l2 = []
			left = 0
			right = k
			# k = (left + right) // 2
			while k > 0:
				hash_dict_s1 = self.precompute_hash(k, self.s, self.poly1[k], self._prime1)
				hash_dict_s2 = self.precompute_hash(k, self.s, self.poly2[k], self._prime2)
				hash_dict_t1 = self.precompute_hash(k, self.t, self.poly1[k], self._prime1)
				hash_dict_t2 = self.precompute_hash(k, self.t, self.poly2[k], self._prime2)
				match1 = self.match_hash(hash_dict_s1, hash_dict_t1, k)
				match2 = self.match_hash(hash_dict_s2, hash_dict_t2, k)
				ans = self.find(match1, match2)
				if len(ans) != 0:
					res[k] = True
					if k == min(self.len_s, self.len_t):
						return ans[-1]
					elif res[k + 1] == False:
						return ans[-1]
					left = k + 1
					k = (left + right) // 2
				else:
					res[k] = False
					right = k - 1
					k = (left + right) // 2
		return Answer(0,0,0)
	
	def match_hash(self, dict_s, dict_t, k):
		if self.flag:
			return [Answer(dict_s[key], dict_t[key], k) for key in list(dict_s.keys() & dict_t.keys())]
		else:
			return [Answer(dict_t[key], dict_s[key], k) for key in list(dict_s.keys() & dict_t.keys())]

	def find(self, l1, l2):
		return [l for l in l1 if l in l2]

	def precompute_hash(self, k, text, y, _prime):
		text_len = len(text)
		str_tmp = text[(text_len - k):text_len]
		hash_l = [-1 for i in range(text_len - k + 1)]

		hash_l[text_len - k] = (self.poly_hash(str_tmp,  _prime), text_len - k)
		for i in range(text_len - k - 1, -1, -1):
			hash_l[i] = ((self._multiplier*hash_l[i+1][0]+ord(text[i])-y*ord(text[i+k]))%_prime, i)
		return dict(hash_l)

	def precompute_poly(self, l, _prime):
		res = []
		for i in range(l):
			res.append(pow(self._multiplier, i, _prime))
		return res
	
	def poly_hash(self, s, _prime):
		ans = 0
		for c in reversed(s):
			ans = (ans * self._multiplier + ord(c)) % _prime # ord() returns Unicode char
		return ans

if __name__ == '__main__':
	for line in sys.stdin.readlines():
		s, t = line.split()
		solver = CommonSubstring(s, t)
		ans = solver.solve()
		print(ans.i, ans.j, ans.len)
