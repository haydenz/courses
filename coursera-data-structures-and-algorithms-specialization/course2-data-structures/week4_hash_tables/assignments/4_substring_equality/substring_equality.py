# python3

import sys

class Solver:
	_multiplier = 99
	_m1 = 1000000007
	_m2 = 1000000009

	def __init__(self, text):
		self.text = text
		self.text_len = len(text)
		self.poly_1 = self.create_poly(self._m1)
		self.poly_2 = self.create_poly(self._m2)
		self.hash_1 = self.precompute_hash(self._m1)
		self.hash_2 = self.precompute_hash(self._m2)

	

	def create_poly(self, _prime):
		poly = [1]
		for i in range(1, self.text_len+1):
			poly.append((poly[i-1] * self._multiplier) % _prime)
		return poly

	def ask(self, a, b, l):
		# return self.text[a:a+l] == self.text[b:b+l]
		H_a_1 = (self.hash_1[a+l] - self.poly_1[l] * self.hash_1[a]) % self._m1
		H_b_1 = (self.hash_1[b+l] - self.poly_1[l] * self.hash_1[b]) % self._m1
		H_a_2 = (self.hash_2[a+l] - self.poly_2[l] * self.hash_2[a]) % self._m2
		H_b_2 = (self.hash_2[b+l] - self.poly_2[l] * self.hash_2[b]) % self._m2
		tmp = (H_a_1 == H_b_1) and (H_a_2 == H_b_2)
		if tmp:
			return True
		else:
			return False

	def fast_hash(self, a, l):
		return self.hash_l[a+l-1] - self.poly[l] * self.hash_l[a-1]

	def precompute_hash(self, _prime):
		hash_l = [-1] * (self.text_len+1)
		# print(self.poly)
		hash_l[0] = 0
		for i in range(1, self.text_len+1):
			hash_l[i] = (hash_l[i-1]*self._multiplier + ord(self.text[i-1])) % _prime
			# print("{}: {}, {}".format(i, hash_l[i], self.poly_hash(self.text[:i+1])))
		return hash_l


	def poly_hash(self, s):
		ans = 0
		for c in s:
			ans = (ans * self._multiplier + ord(c)) #% self._prime # ord() returns Unicode char
		return ans

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	# for a in range(len(s)):
	# 	for b in range(len(s)):
	# 		for l in range(1, len(s)):
	# 			solver.ask(a, b, min(len(s) - max(a, b) - 1, l))
	print("Yes" if solver.ask(a, b, l) else "No")
