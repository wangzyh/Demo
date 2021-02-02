# Queue


class QueueNode():
    def __init__(self):
        self.rear = 0
        self.front = -1
        self.q = []
        self.max_size = 100

    def add_q(self, item):
        if (self.rear + 1) % self.max_size == self.front:
            print("队列满")
            return
        self.rear = (self.rear + 1) % self.max_size
        self.q[self.rear] = item

    def delete_q(self):
        if self.front == self.rear:
            print("队列空")
            return IndexError
        else:
            self.front = (self.front + 1) % self.max_size
            return self.q[self.front]
