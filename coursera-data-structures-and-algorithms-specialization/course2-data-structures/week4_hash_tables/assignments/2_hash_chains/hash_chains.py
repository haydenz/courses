# python3

''' Hints
1. Beware of integer overflow. Use long long type in C++ and long type in Java where appropriate. Take
everything (mod 𝑝) as soon as possible while computing something (mod 𝑝), so that the numbers are
always between 0 and 𝑝 − 1.
2. Beware of taking negative numbers (mod 𝑝). In many programming languages, (−2)%5 ̸= 3%5. Thus
you can compute the same hash values for two strings, but when you compare them, they appear to
be different. To avoid this issue, you can use such construct in the code: 𝑥 ← ((𝑎%𝑝) + 𝑝)%𝑝 instead
of just 𝑥 ← 𝑎%𝑝.
'''


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(bucket_count)]
        self.hashes = dict()

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime # ord() returns Unicode char
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        if len(chain) != 0:
            print(' '.join(reversed(chain)))
        else:
            print('')

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # self.write_chain(cur for cur in reversed(self.elems) 
            #             if self._hash_func(cur) == query.ind)
            self.write_chain(self.elems[query.ind])
        else:
            # try:
            #     ind = self.elems.index(query.s)
            # except ValueError:
            #     ind = -1
            try:
                ind = self.hashes[query.s]
            except KeyError:
                ind = -1
            # exist = [query.s in l for l in self.elems]
            # if any(exist):
            #     ind = exist.index(True)
            # else:
            #     ind = -1

            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    hash_idx = self._hash_func(query.s)
                    self.elems[hash_idx].append(query.s)
                    self.hashes.update({query.s: hash_idx})
            else: # query.type == 'del'
                if ind != -1:
                    self.elems[ind].remove(query.s)
                    self.hashes.pop(query.s)

    def process_queries(self):
        n = int(input())
        # n = 12
        # tmp = [('check',0), ('find', 'help'), ('add', 'help'),
        #        ('add', 'del'), ('add', 'add'), ('find', 'add'),
        #        ('find', 'del'), ('del', 'del'), ('find', 'del'),
        #        ('check', 0), ('check', 1), ('check', 2)]
        for i in range(n):
            self.process_query(self.read_query())
            # self.process_query(Query(tmp[i]))

if __name__ == '__main__':
    bucket_count = int(input())
    # bucket_count = 3
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
