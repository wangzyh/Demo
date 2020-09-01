# Definition for a binary tree node.
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)


def traverse(root: TreeNode):
    if root:
        traverse(root.left)
        traverse(root.right)
        print(root.val)


def in_order_traversal(root: TreeNode):
    t = root
    s = []
    while t or s:
        while t:
            s.append(t)
            print(t.val)  # 前序
            t = t.left
        if s:
            t = s[-1]
            s.pop(-1)  # 中序
            # print(t.val)  # 中序
            t = t.right


def level_order_traversal(root: TreeNode):
    if not root:
        return
    q = Queue()
    q.put(root)
    while not q.empty():
        t = q.get()
        print(t.val)
        if t.left:
            q.put(t.left)
        if t.right:
            q.put(t.right)


def get_height(root: TreeNode):
    if root:
        hl = get_height(root.left)
        hr = get_height(root.right)
        maxh = max(hl, hr)
        return maxh + 1
    else:
        return 0


def isSameTree(root):
    pass


# [3,9,20,null,null,15,7]
# [3,9,20,1,null,15,7,1,1]

def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            print(line)
            node = stringToTreeNode(line)
            prettyPrintTree(node)

            res = isSameTree(node)
            print(str(res))

        except StopIteration:
            break


if __name__ == '__main__':
    main()
