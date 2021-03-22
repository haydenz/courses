# python3

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__auxiliary = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__auxiliary) > 0:
            self.__auxiliary.append(max(a, self.__auxiliary[-1]))
        else:
            self.__auxiliary.append(a)

    def Pop(self):
        assert(len(self.__auxiliary))
        self.__auxiliary.pop()
        assert(len(self.__stack))
        return self.__stack.pop()

    def Max(self):
        assert(len(self.__auxiliary))
        return self.__auxiliary[-1]

    def size(self):
        return len(self.__stack)

class queueByStack():
    def __init__(self, m):
        self.__s1 = StackWithMax()
        self.__s2 = StackWithMax()
        self.m = m
    
    def enqueue(self, a):
        self.__s2.Push(a)
    
    def dequeue(self, i):
        if self.__s1.size() == 0:
            while self.__s2.size() != 0:
                self.__s1.Push(self.__s2.Pop())
            if i > self.m-1:
                self.__s1.Pop()
        else:
            self.__s1.Pop()
    
    def getMax(self):
        if self.__s1.size() != 0:
            if self.__s2.size() != 0:
                return max(self.__s1.Max(), self.__s2.Max())
            else:
                return self.__s1.Max()              
        return self.__s2.Max()

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    def push(self, newTail):
        self.tail.prev.next = newTail
        self.tail.prev.next.next = Node(None)

    def popFront(self):
        oldHead = self.head.next.data
        self.head.next = self.head.next.next
        return oldHead

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

#######################
#    Method 1
#######################
def implement_queue_using_two_stacks(sequence, m):
    q = queueByStack(m)
    maximums = []
    for i in range(len(sequence)):
        if i < m:
            q.enqueue(sequence[i])
            if i == m-1:
                q.dequeue(i)
                maximums.append(q.getMax())
        else:
            q.dequeue(i)
            q.enqueue(sequence[i])
            maximums.append(q.getMax())
    return maximums

#######################
#    Method 2
#######################
def preprocess_block_suffixes_and_prefixes(sequence, m):
    l = DoublyLinkedList()
    for i in range(len(sequence)):
        # TODO:
        pass

#######################
#    Method 3
#######################
def store_relevant_items_in_a_dequeue(sequence, m):
    pass

if __name__ == '__main__':
    n = int(input())
    # n = 6
    input_sequence = [int(i) for i in input().split()]
    # input_sequence = [6,5,4,3,2,1]
    
    assert len(input_sequence) == n
    window_size = int(input())
    # window_size = 1

    # print(*max_sliding_window_naive(input_sequence, window_size))
    print(*implement_queue_using_two_stacks(input_sequence, window_size), sep=' ')
    # print(*preprocess_block_suffixes_and_prefixes(input_sequence, window_size))
    # print(*store_relevant_items_in_a_dequeue(input_sequence, window_size))

