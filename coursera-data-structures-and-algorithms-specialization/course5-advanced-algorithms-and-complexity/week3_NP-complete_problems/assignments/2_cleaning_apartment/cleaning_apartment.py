# python3

import itertools


def read_inputs():
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    return n,m,edges

def printEquisatisfiableSatFormula(n,m,edges):
    clauses = []
    positions = range(1, n + 1)
    adj = [[] for _ in range(n)]
    for i, j in edges:
        adj[i - 1].append(j - 1)
        adj[j - 1].append(i - 1)

    for i in range(n):
        exactly_One_Of([var_number(i, j) for j in positions], clauses)

    for j in positions:
        exactly_One_Of([var_number(i, j) for i in range(n)], clauses)

    for j in positions[:-1]:
        for i, nodes in enumerate(adj):
            clauses.append([-var_number(i, j)] + [var_number(n, j + 1) for n in nodes])

    print(len(clauses), n * n)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))

def var_number(i, j):
    return n*i + j

def exactly_One_Of(literals, clauses):
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

if __name__ == '__main__':
    n,m,edges = read_inputs()
    printEquisatisfiableSatFormula(n,m,edges)

