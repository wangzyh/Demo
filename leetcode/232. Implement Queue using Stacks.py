# 232. Implement Queue using Stacks
# 2020/7/6


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isempty = 0
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q.append(x)
        self.isempty += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.isempty -= 1
        return self.q.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not bool(self.isempty)


if __name__ == '__main__':

    queue = MyQueue()
    print(queue.push(1))
    print(queue.push(2))
    print(queue.pop())
    print(queue.peek())
    print(queue.empty())

