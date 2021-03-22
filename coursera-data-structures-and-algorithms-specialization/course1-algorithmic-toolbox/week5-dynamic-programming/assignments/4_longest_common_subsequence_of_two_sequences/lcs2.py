#Uses python3

import sys
import numpy as np

def lcs2(a, b):
    m = len(a)
    n = len(b)

    recorded_map = np.zeros((m + 1, n + 1))
    # print(recorded_map.shape)

    for i, a_ in enumerate(a):
        for j, b_ in enumerate(b):
            # print(i,j)
            if a_ == b_:
                # print(a[i], b[j])
                recorded_map[i+1][j+1] = recorded_map[i][j]+1
            else:
                recorded_map[i+1][j+1] = max(recorded_map[i+1][j], recorded_map[i][j+1])
    # print(recorded_map)
    return int(recorded_map[m][n])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
    # print(lcs2([1,2,3], [3,2,1]))
