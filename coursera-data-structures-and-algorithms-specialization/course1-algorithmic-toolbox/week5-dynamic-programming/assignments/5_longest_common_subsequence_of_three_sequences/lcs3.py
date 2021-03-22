#Uses python3

import sys
import numpy as np

def lcs3(a, b, c):
    recorded_map = np.zeros((len(a) + 1, len(b) + 1, len(c) + 1))

    for i, a_ in enumerate(a):
        for j, b_ in enumerate(b):
            for k , c_ in enumerate(c):
                if a_ == b_ and a_ == c_:
                    # print(a_, b_, c_)
                    recorded_map[i+1][j+1][k+1] = recorded_map[i][j][k]+1
                else:
                    recorded_map[i+1][j+1][k+1] = max(recorded_map[i+1][j+1][k], recorded_map[i][j+1][k+1], recorded_map[i+1][j][k+1])
    # print(recorded_map)
    return int(recorded_map[len(a)][len(b)][len(c)])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
