# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, dst, src):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[src_parent])
        else:
            self.parents[src_parent] = dst_parent
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent] += 1
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])
        # self.max_row_count = max(self.row_counts)
        # print("source: {}, source_parent: {}, source_parent_rank: {}\ndestination: {}, destination_parent: {}, destination_parent_rank: {}".format(src, src_parent, self.ranks[src_parent], dst, dst_parent, self.ranks[dst_parent]))

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return True

    def get_parent(self, idx):
        # find parent and compress path
        if self.parents[idx] != idx:
            self.parents[idx] = self.get_parent(self.parents[idx])
        return self.parents[idx]


def main():
    n_tables, n_queries = map(int, input().split())
    # n_tables, n_queries = 5,5
    counts = list(map(int, input().split()))
    # counts = [1] * 5
    # tmp = [(3,5),(2,4),(1,4),(5,4),(5,3)]
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        # dst, src = tmp[i]
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)

if __name__ == "__main__":
    main()
