# Uses python3
import sys

def optimal_sequence(n):
    operation_num = [0, 1] + [0] * (n-1)

    for i in range(2, n+1):
        count_idx = [i-1]
        if i % 2 == 0:
            count_idx.append(i // 2)
        if i % 3 == 0:
            count_idx.append(i // 3)
        
        operation_num[i] = 1 + min([operation_num[c] for c in count_idx])
    # print(operation_num)
    current_val = n
    res = [current_val]
    while current_val != 1:
        tmp = [current_val - 1]
        if current_val % 2 == 0:
            tmp.append(current_val // 2)
        if current_val % 3 == 0:
            tmp.append(current_val // 3)
        
        current_val = min([(t, operation_num[t]) for t in tmp], key=lambda x: x[1])[0]
        res.append(current_val)

    return reversed(res)

input = sys.stdin.read()
n = int(input)
# n = 96234
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
