# python3
import copy
from sys import stdin

EPS = 1e-6
PRECISION = 20


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def ReadEquation():
    size = int(input())  # The number of dishes in the menu
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))  # the amount of ingredient and est total energy value
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


def SelectPivotElement(a, used_rows, used_columns):
    # Select the first free element.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1

    # Update the pivot with the largest abs value
    _max = 0
    for i in range(pivot_element.row, len(a)):
        if abs(a[i][pivot_element.column]) > abs(_max):
            _max = a[i][pivot_element.column]
            pivot_element.row = i

    while a[pivot_element.row][pivot_element.column] == 0 or used_rows[pivot_element.row]:
        pivot_element.row += 1
        if pivot_element.row > len(a) - 1:
            return None

    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[
        pivot_element.column]
    pivot_element.row = pivot_element.column;


def ScalePivot(a, b, pivot_element):
    ncol = len(a[0])
    div = a[pivot_element.row][pivot_element.column]
    for j in range(pivot_element.column, ncol):
        a[pivot_element.row][j] /= div
    b[pivot_element.row] /= div
    return a, b


def ProcessPivotElement(a, b, pivot_element):
    nrow = len(a)
    ncol = len(a[0])
    a, b = ScalePivot(a, b, pivot_element)

    for i in range(pivot_element.row + 1, nrow):
        mult = a[i][pivot_element.column]
        for j in range(pivot_element.column, ncol):
            a[i][j] -= a[pivot_element.row][j] * mult
        b[i] -= b[pivot_element.row] * mult


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def BackSubstitution(a, b):
    # Assume m = n
    nrow = len(a)
    for i in range(nrow - 1, 0, -1):
        tmp = b[i]
        for j in range(i):
            b[j] -= a[j][i] * tmp
            a[j][i] = 0
    return 0


def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        if pivot_element is None:
            return False, None
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    BackSubstitution(a, b)

    return True, b


def checkResult(n, m, A, b, c, result, lastEquation, ans, bestScore):
    for r in result:
        if r < -1e-3:
            return False, ans, bestScore
    for i in range(n):
        r = 0.0
        for j in range(m):
            r += A[i][j] * result[j]
        if r > b[i] + 1e-3:
            return False, ans, bestScore
    score = 0.0
    for j in range(m):
        score += c[j] * result[j]
    if score <= bestScore:
        return False, ans, bestScore
    else:
        if lastEquation:
            return True, 1, score
        else:
            return True, 0, score


def preprocess(n, m, A, b):
    # # Assume n = m
    for i in range(m):
        tmp = [0 for _ in range(len(A[0]))]
        tmp[i] = -1
        A.append(tmp)
        b.append(-0.0)

    A.append([1 for _ in range(len(A[0]))])
    b.append(1.0e9)


def solve_diet_problem(n, m, A, b, c):
    # solve x: vector of length m with amounts of each ingredient
    preprocess(n, m, A, b)
    l = n + m + 1
    ans = -1
    bestScore = -float('inf')
    bestResult = None
    for x in range(2 ** l):
        usedIndex = [i for i in range(l) if ((x / 2 ** i) % 2) // 1 == 1]
        if len(usedIndex) != m:
            continue
        lastEquation = False
        if usedIndex[-1] == l - 1:
            lastEquation = True
        As = [A[i] for i in usedIndex]
        bs = [b[i] for i in usedIndex]
        solved, result = SolveEquation(copy.deepcopy(Equation(As, bs)))
        if solved:
            isAccepted, ans, bestScore = checkResult(n, m, A, b, c, result, lastEquation, ans, bestScore)
            if isAccepted:
                bestResult = result
    return [ans, bestResult]


def read_inputs():
    # n=number of restrictions on your diet
    # m=number of all available dishes an drinks
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
        A += [list(map(int, stdin.readline().split()))]
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    return n, m, A, b, c


def print_sol(anst, ansx):
    if anst == -1:
        print("No solution")
    if anst == 0:
        print("Bounded solution")
        print(' '.join(['%.18f' % a for a in ansx]))
    if anst == 1:
        print("Infinity")


if __name__ == '__main__':
    n, m, A, b, c = read_inputs()
    anst, ansx = solve_diet_problem(n, m, A, b, c)
    print_sol(anst, ansx)
