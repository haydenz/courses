#python3
import sys

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
        assert(len(self.__stack))
        self.__stack.pop()
        assert(len(self.__auxiliary))
        self.__auxiliary.pop()

    def Max(self):
        assert(len(self.__auxiliary))
        # tmp = self.__auxiliary[]
        return self.__auxiliary[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
