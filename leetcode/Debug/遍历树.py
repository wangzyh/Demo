from typing import List

from tree import stringToTreeNode, TreeNode


# region 前序
def preorder(root):
    if root is None:
        return ''
    print(root.val)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


# endregion

# region 中序
def midorder(root):
    if root is None:
        return ''
    if root.left:
        midorder(root.left)
    print(root.val)
    if root.right:
        midorder(root.right)


# endregion

# region 后续
def endorder(root):
    if root is None:
        return ''
    if root.left:
        endorder(root.left)
    if root.right:
        endorder(root.right)
    print(root.val)


# endregion

# region 广度优先
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


# endregion

# region 获取路径
def get_path(root: TreeNode) -> List:
    if not root:
        return []
    elif not root.left and not root.right:
        return [root.val]
    else:

        ll = get_path(root.left)
        rl = get_path(root.right)
        return [[root.val] + ([i] if isinstance(i, int) else i) for i in ll + rl]


# endregion


if __name__ == '__main__':
    tree = '[4,2,6,1,3,null,null]'
    root = stringToTreeNode(tree)
    # preorder(root)
    # midorder(root)
    # endorder(root)
    # graorder(root)
    print(get_path(root))
