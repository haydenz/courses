# python3

def left_child(i, data):
    if 2*(i+1) - 1 >= len(data):
        return i
    else:
        return 2*(i+1) - 1

def right_child(i, data):
    if 2*(i+1) >= len(data):
        return i
    else:
        return 2*(i+1)

def shift_up(i, data, swaps):
    min_idx = i
    l = left_child(i, data)
    r = right_child(i, data)

    if l <= len(data) - 1 and data[l] < data[min_idx]:
        min_idx = l
    
    if r <= len(data) - 1 and data[r] < data[min_idx]:
        min_idx = r

    if i != min_idx:
        swaps.append((i, min_idx))
        data[i], data[min_idx] = data[min_idx], data[i]
        shift_up(min_idx, data, swaps)

def efficient_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        shift_up(i, data, swaps)
    return swaps

    
def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps




def main():
    n = int(input())
    # n = 5
    data = list(map(int, input().split()))
    # data = [1,2,3,4,5]
    assert len(data) == n

    swaps = efficient_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
