# Find the sum of all left leaves in a given binary tree. 
# 
#  Example:
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15 respectivel
# y. Return 24.
#  
#  Related Topics Tree 
#  👍 1765 👎 167

# region time
# 2021-03-30 20:40:49
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Debug.tree import TreeNode, stringToTreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = [root]
        while queue:
            node = queue.pop()
            if node.left:
                if node.left.left is None and node.left.right is None:
                    res += node.left.val
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = stringToTreeNode('[1,2,3,4,5,6,34,3,2,1,23,3,34]')
    print(Solution().sumOfLeftLeaves(n))
