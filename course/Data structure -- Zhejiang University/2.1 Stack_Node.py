# 堆栈


class SNode:
    def __init__(self):
        self.node = list()
        self.max_size = 100
        self.top = -1

    # 入栈
    def push(self, item):
        if self.top == self.max_size - 1:
            print("堆栈满")
            return
        else:
            self.node.append(item)
            self.top += 1

    def pop(self):
        if self.top == -1:
            print("堆栈空")
            return IndexError
        else:
            self.node.pop(-1)
            self.top -= 1



