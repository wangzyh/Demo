# 155. Min Stack
# 2020/7/5


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_s = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_s = min(self.min_s, x) if self.min_s != None else x

    def pop(self) -> None:
        self.stack.pop()
        self.min_s = min(self.stack) if self.stack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_s


if __name__ == '__main__':
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
    # print(minStack.push(-1))
    # print(minStack.top())
    # print(minStack.getMin())
