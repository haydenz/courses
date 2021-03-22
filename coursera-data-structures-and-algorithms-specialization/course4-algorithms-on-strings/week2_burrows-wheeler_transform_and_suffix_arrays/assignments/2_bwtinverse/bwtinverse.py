# python3
import sys

def EfficientInverseBWT(bwt):
    sorted_bwt = sorted([(b, i) for i, b in enumerate(bwt)])

    k = bwt.index("$")
    res = ""
    for _ in range(len(bwt)):
        t, k = sorted_bwt[k]
        res += t
    return res

def NaiveInverseBWT(bwt):
    # write your code here
    # Sort len(bwt) - 1 times
    bwt_len = len(bwt)
    first_cols = sorted(bwt)
    for i in range(bwt_len-1):
        first_cols = sorted([bwt[i] + first_cols[i] for i in range(bwt_len)])

    return first_cols[0][1:] + "$"


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(EfficientInverseBWT(bwt))