# python3
from sys import stdin

def read_inputs():
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
        A += [list(map(int, stdin.readline().split()))]
    b = list(map(int, stdin.readline().split()))
    return n,m,A,b

def printEquisatisfiableSatFormula(n,m,A,b):
    clauses = []
    for i, coefficient in enumerate(A):
        non0coeffs = [(j, coefficient[j]) for j in range(m) if 0 != coefficient[j]]
        l = len(non0coeffs)
        for x in range(2 ** l):
            currSet = [non0coeffs[j] for j in range(l) if 1 == ((x / 2 ** j) % 2) // 1]
            currSum = 0
            for coeff in currSet:
                currSum += coeff[1]
            if currSum > b[i]:
                clauses.append([-(coeff[0] + 1) for coeff in currSet] + [coeff[0] + 1 for coeff in non0coeffs if
                                                                         not coeff in currSet])

    if 0 == len(clauses):
        clauses.append([1, -1])
        m = 1
    print(len(clauses), m)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))

if __name__ == '__main__':
    n,m,A,b = read_inputs()
    printEquisatisfiableSatFormula(n, m, A, b)