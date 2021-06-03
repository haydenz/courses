# python3
import sys


def sort_char(s):
    letter_map = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
    order = [None] * len(s)
    count = [0] * 5
    for i in range(len(s)):
        idx = letter_map[s[i]]
        count[idx] = count[idx] + 1
    for i in range(1, 5):
        count[i] = count[i] + count[i - 1]
    for i in reversed(range(len(s))):
        c = s[i]
        idx = letter_map[c]
        count[idx] = count[idx] - 1
        order[count[idx]] = i
    return order


def char_classes(s, order):
    cl = [None] * len(s)
    cl[order[0]] = 0
    for i in range(1, len(s)):
        if s[order[i]] != s[order[i - 1]]:
            cl[order[i]] = cl[order[i - 1]] + 1
        else:
            cl[order[i]] = cl[order[i - 1]]
    return cl


def sort_doubled(s, l, order, cl):
    count = [0] * len(s)
    new_order = [None] * len(s)
    for i in range(len(s)):
        count[cl[i]] = count[cl[i]] + 1
    for i in range(1, len(s)):
        count[i] = count[i] + count[i - 1]
    for i in reversed(range(len(s))):
        start = (order[i] - l) % len(s)
        c = cl[start]
        count[c] = count[c] - 1
        new_order[count[c]] = start
    return new_order


def update_classes(new_order, n, cl, l):
    new_cl = [None] * n
    new_cl[new_order[0]] = 0
    for i in range(1, n):
        cur, prev = new_order[i], new_order[i - 1]
        mid, midprev = (cur + l) % n, (prev + l) % n
        if cl[cur] != cl[prev] or cl[mid] != cl[midprev]:
            new_cl[cur] = new_cl[prev] + 1
        else:
            new_cl[cur] = new_cl[prev]
    return new_cl


def build_suffix_array(s):
    order = sort_char(s)
    cl = char_classes(s, order)
    l = 1
    while l < len(s):
        order = sort_doubled(s, l, order, cl)
        cl = update_classes(order, cl, l)
        l *= 2
    return order


def is_less_than(p, s, i):
    for idx, c in enumerate(p):
        c2 = s[i + idx]
        if c == c2:
            continue
        elif c < s[i + idx]:
            return True
        else:
            return False
    return False


def is_greater_than(p, s, i):
    for idx, c in enumerate(p):
        c2 = s[i + idx]
        if c == c2:
            continue
        elif c > s[i + idx]:
            return True
        else:
            return False
    return False


def find_occurrences(text, patterns):
    s = text + '$'
    suffix_array = build_suffix_array(s)

    occs = set()
    for p in patterns:
        min_idx = 0
        max_idx = len(s)
        while min_idx < max_idx:
            mid_idx = (min_idx + max_idx) // 2
            if is_greater_than(p, s, suffix_array[mid_idx]):
                min_idx = mid_idx + 1
            else:
                max_idx = mid_idx
        start = min_idx
        max_idx = len(s)

        while min_idx < max_idx:
            mid_idx = (min_idx + max_idx) // 2
            if is_less_than(p, s, suffix_array[mid_idx]):
                max_idx = mid_idx
            else:
                min_idx = mid_idx + 1
        end = max_idx
        if start > end:
            continue
        else:
            for i in range(start, end):
                occs.add(suffix_array[i])
    return occs


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))