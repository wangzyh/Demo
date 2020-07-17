# 225. Implement Stack using Queues
# 2020/7/14


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.is_empty = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        self.is_empty += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        last = self.stack[-1]
        self.stack.pop(-1)
        self.is_empty -= 1
        return last

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.is_empty)


if __name__ == '__main__':
    stack = MyStack()

    print(stack.push(1))
    print(stack.push(2))
    print(stack.top())
    print(stack.pop())
    print(stack.empty())
