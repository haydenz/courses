# Uses python3
import sys
import itertools
import numpy as np


def partition3(A): # discrete, w/o repetition
    # write your code here
    if sum(A) % 3 != 0:
        return '0'
    W = sum(A) // 3
    w = A
    dp = np.zeros((W+1, len(w)+1))
    count = 0
    for j in range(1, len(w)+1):
        for w_i in range(1, W+1):
            dp[w_i][j] = dp[w_i][j-1]
            if w[j-1] <= w_i:
                val = dp[w_i - w[j-1]][j-1] + w[j-1]
                if dp[w_i][j] < val:
                    dp[w_i][j] = val
            if dp[w_i][j] == W:
                count += 1
    if count < 3:
        return '0'
    else:
        return '1'

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

