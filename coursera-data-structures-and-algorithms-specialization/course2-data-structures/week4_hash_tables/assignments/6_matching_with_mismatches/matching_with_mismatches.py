# python3

import sys

def solve(k, text, pattern):
	return []

class Mismatch:
	_multiplier = 113
	_prime1 = 1000000007
	_prime2 = 1000000009

	def __init__(self, no_mismatch, text, pattern):
		self.no_mismatch = no_mismatch
		self.t = text
		self.p = pattern
		self.prefix_t1 = self.prefix_hash(self.t, self._prime1)
		self.prefix_t2 = self.prefix_hash(self.t, self._prime2)
		self.prefix_p1 = self.prefix_hash(self.p, self._prime1)
		self.prefix_p2 = self.prefix_hash(self.p, self._prime2)
		self.poly1 = self.precompute_poly(len(self.p)+1, self._prime1)
		self.poly2 = self.precompute_poly(len(self.p)+1, self._prime2)
	
	def solve(self):
		res = []
		hash_p1 = self.prefix_p1[len(self.p)] - self.poly1[len(self.p)] * self.prefix_p1[1]
		hash_p2 = self.prefix_p2[len(self.p)] - self.poly2[len(self.p)] * self.prefix_p2[1]
		for i in range(0, len(self.t) - len(self.p) + 1):
			hash_t1 = self.prefix_t1[i+len(self.p)] - self.poly1[len(self.p)] * self.prefix_t1[i]
			hash_t2 = self.prefix_t2[i+len(self.p)] - self.poly2[len(self.p)] * self.prefix_t2[i]
			
			if hash_t1 == hash_p1 and hash_t2 == hash_p2:
				continue
			else:
				mis = self.count_mismatch(left=i+1, right=i+len(self.p), pos=i)
				if mis <= self.no_mismatch:
					res.append(i)
		return res

	def count_mismatch(self, left, right, pos):
		mid = (left + right) // 2
		left_p = left - pos
		right_p = right - pos
		mid_p = (left_p + right_p) // 2

		hash_t1 = (self.prefix_t1[mid] - self.poly1[1] * self.prefix_t1[mid-1]) % self._prime1
		hash_p1 = (self.prefix_p1[mid_p] - self.poly1[1] * self.prefix_p1[mid_p-1]) % self._prime1
		hash_t2 = (self.prefix_t2[mid] - self.poly2[1] * self.prefix_t2[mid-1]) % self._prime2
		hash_p2 = (self.prefix_p2[mid_p] - self.poly2[1] * self.prefix_p2[mid_p-1]) % self._prime2
		if hash_t1 == hash_p1 and hash_t2 == hash_p2:
			count = 0
		else:
			count = 1
			
		if mid-1 >= left:
			left_ask = self.substring_ask(left=left, right=mid-1, left_p=left_p, right_p=mid_p-1)
			if not left_ask:
				count += self.count_mismatch(left=left, right=mid-1, pos=pos)
				if count > self.no_mismatch:
					return count
		
		if right >= mid+1:
			right_ask = self.substring_ask(left=mid+1, right=right, left_p=mid_p+1, right_p=right_p)
			if not right_ask:
				count += self.count_mismatch(left=mid+1, right=right, pos=pos)
				if count > self.no_mismatch:
					return count

		return count
	
	def substring_ask(self, left, right, left_p, right_p):
		l = right - left + 1
		hash_t1 = (self.prefix_t1[right] - self.poly1[l] * self.prefix_t1[left-1]) % self._prime1
		hash_p1 = (self.prefix_p1[right_p] - self.poly1[l] * self.prefix_p1[left_p-1]) % self._prime1
		hash_t2 = (self.prefix_t2[right] - self.poly2[l] * self.prefix_t2[left-1]) % self._prime2
		hash_p2 = (self.prefix_p2[right_p] - self.poly2[l] * self.prefix_p2[left_p-1]) % self._prime2
		tmp = (hash_t1== hash_p1) and (hash_t2 == hash_p2)
		if tmp:
			return True
		else:
			return False
	
	def prefix_hash(self, text, _prime):
		hash_l = [-1] * (len(text)+1)
		hash_l[0] = 0
		for i in range(1, len(text)+1):
			hash_l[i] = (hash_l[i-1]*self._multiplier + ord(text[i-1])) % _prime
		return hash_l
	
	def precompute_poly(self, l, _prime):
		return [pow(self._multiplier, i, _prime) for i in range(l)]


for line in sys.stdin.readlines():
	k, t, p = line.split()
	mis = Mismatch(int(k), t, p)
	ans = mis.solve()
	# print(ans)
	if len(ans) == 0:
		print(0)	
	else:
		print(len(ans), *ans)
