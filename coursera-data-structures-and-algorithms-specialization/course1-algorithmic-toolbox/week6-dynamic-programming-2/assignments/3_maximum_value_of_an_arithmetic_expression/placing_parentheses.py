# Uses python3
import math 
import numpy as np

def evalt(a, b, op):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)
    else:
        assert False

def min_and_max(i,j, digits, ops, dp_m, dp_M):
    min_ = math.inf
    max_ = - math.inf

    for k in range(i, j):
        a = evalt(dp_M[i][k], dp_m[k+1][j], ops[k])
        # print("k = {}, ops = {}".format(k, ops[k]))
        b = evalt(dp_M[i][k], dp_M[k+1][j], ops[k])
        c = evalt(dp_m[i][k], dp_m[k+1][j], ops[k])
        d = evalt(dp_m[i][k], dp_M[k+1][j], ops[k])
        min_ = min(min_, a, b, c, d)
        max_ = max(max_, a, b, c, d)
    return min_, max_

def get_maximum_value(dataset):
    digits = []
    ops = []
    for i, d in enumerate(dataset):
        if i % 2 == 0:
            digits.append(int(d))
        else:
            ops.append(d)
    n = len(digits)
    # print(digits)
    # print(ops)
    dp_m = np.zeros((n,n))
    dp_M = np.zeros((n,n))

    for i in range(n):
        dp_m[i][i] = digits[i]
        dp_M[i][i] = digits[i]

    for s in range(1,n):
        for i in range(0, n-s):
            j = i+s
            dp_m[i][j], dp_M[i][j] = min_and_max(i, j, digits, ops, dp_m, dp_M)
    # print(dp_m)
    # print(dp_M)
    return int(dp_M[0][n-1])


if __name__ == "__main__":
    print(get_maximum_value(input()))
    # print(get_maximum_value("5-8+7*4-8+9"))
