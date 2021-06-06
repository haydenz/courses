# python3

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
    size = int(input()) # The number of dishes in the menu
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split())) # the amount of ingredient and est total energy value
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

    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
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

    for i in range(pivot_element.row+1, nrow):
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
    for i in range(nrow-1, 0, -1):
        tmp = b[i]
        for j in range(i):
            b[j] -= a[j][i] * tmp
            a[j][i] = 0

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    BackSubstitution(a, b)

    return b

def PrintColumn(column):
    print(' '.join(['%.20lf' % c for c in column]))

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
