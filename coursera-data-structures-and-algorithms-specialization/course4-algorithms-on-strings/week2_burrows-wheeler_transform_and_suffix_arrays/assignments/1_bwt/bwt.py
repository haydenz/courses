# python3
import sys

def NaiveBWT(text):
    # Calculate all cyclic rotations
    cyclic_rotations = []
    for i in range(len(text)-1,-1,-1):
        cyclic_rotations.append(text[i:] + text[:i])

    # Extract the final char of sorted cyclic rotations
    res = ""
    for c in sorted(cyclic_rotations):
        res += c[-1]

    return res

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(NaiveBWT(text))