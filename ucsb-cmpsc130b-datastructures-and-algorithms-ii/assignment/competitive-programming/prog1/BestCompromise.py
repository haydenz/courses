'''
https://open.kattis.com/problems/compromise
'''
import sys

def count_zeros_ones(binary, m, n):
    # use summation to speed up
    ones = [sum(binary[i][j] for i in range(n)) for j in range(m)]
    count = dict((i, [n-ones[i], ones[i]]) for i in range(m))
    return count

def max_counted_str(count):
    res = ["1" if count[i][0] < count[i][1] else "0" for i in count] 
    return "".join(res)

if __name__ == '__main__':
    # read the first line -- number of test scenarios
    test = int(sys.stdin.readline())
    # empty list to store results to be printed
    res = []

    for _ in range(test):
        # read the number of ppl n, and number of different issues m
        n, m = [int(x) for x in sys.stdin.readline().split()]
        # empty list to store matrix input
        binary = []
        for i in range(n):
            binary.append([int(b) for b in sys.stdin.readline()[:-1]])
        # count number of zeros and ones for each row and col in the matrix
        count = count_zeros_ones(binary, m, n)
        # append string answer for this test scenario
        res.append(max_counted_str(count))
    
    for r in res:
        print(r)
