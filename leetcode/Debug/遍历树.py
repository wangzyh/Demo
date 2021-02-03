from tree import stringToTreeNode


# 前序
def preorder(root):
    if root is None:
        return ''
    print(root.val)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


# 中序
def midorder(root):
    if root is None:
        return ''
    if root.left:
        midorder(root.left)
    print(root.val)
    if root.right:
        midorder(root.right)


# 后续
def endorder(root):
    if root is None:
        return ''
    if root.left:
        endorder(root.left)
    if root.right:
        endorder(root.right)
    print(root.val)


# 广度优先
# 根节点 -> 左节点 -> 右节点
def graorder(root):
    if root is None:
        return ''
    queue = [root]
    while queue:
        res = []
        for item in queue:
            print(item.val)
            if item.left:
                res.append(item.left)
            if item.right:
                res.append(item.right)
        queue = res


if __name__ == '__main__':
    tree = '[4,2,6,1,3,null,null]'
    root = stringToTreeNode(tree)
    preorder(root)
    print(111)
    midorder(root)
    print(2222)
    endorder(root)
    print(333)
    graorder(root)
