# Uses python3
import numpy as np

def edit_distance(s, t):
    n = len(s)
    m = len(t)

    recorded_map = np.zeros((m + 1, n + 1))
    for j in range(n+ 1):
        recorded_map[0][j] = j
    for i in range(m+1):
        recorded_map[i][0] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            insertion = recorded_map[i-1][j] + 1
            deleltion = recorded_map[i][j-1] + 1
            mismatch = recorded_map[i-1][j-1] + 1
            match = recorded_map[i-1][j-1]
            if s[j-1] == t[i-1]:
                recorded_map[i][j] = min(insertion, deleltion, match)
            else:
                recorded_map[i][j] = min(insertion, deleltion, mismatch)
    # print(recorded_map)
    return int(recorded_map[m][n])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance('editing', 'distance'))
