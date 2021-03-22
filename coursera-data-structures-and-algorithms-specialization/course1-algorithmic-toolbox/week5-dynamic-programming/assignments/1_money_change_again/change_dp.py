# Uses python3
import sys

def get_change(m):
    res = [0] + [-1]*m
    denominators = [1,3,4]
    for i in range(1, m+1):
        for j in denominators:
            if i >= j:
                coins = res[i-j]+1
                if (res[i] == -1) or (coins < res[i]):
                    res[i] = coins
    return res[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
