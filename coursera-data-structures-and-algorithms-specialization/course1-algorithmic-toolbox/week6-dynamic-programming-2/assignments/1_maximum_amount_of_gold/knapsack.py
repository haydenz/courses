# Uses python3
import sys
import numpy as np

def optimal_weight(W, w): # discrete, w/o repetition
    # write your code here
    dp = np.zeros((W+1, len(w)+1))

    for i in range(W+1):
        dp[i][0] = 0
    for i in range(len(w)+1):
        dp[0][i] = 0

    for i in range(1, len(w)+1):
        for w_i in range(1, W+1):
            dp[w_i][i] = dp[w_i][i-1]
            if w[i-1] <= w_i:
                val = dp[w_i - w[i-1]][i-1] + w[i-1]
                if dp[w_i][i] < val:
                    dp[w_i][i] = val
    return int(dp[W][len(w)])

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
