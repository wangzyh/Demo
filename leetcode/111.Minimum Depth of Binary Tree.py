# Given a binary tree, find its minimum depth. 
# 
#  The minimum depth is the number of nodes along the shortest path from the roo
# t node down to the nearest leaf node. 
# 
#  Note: A leaf is a node with no children. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 105]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics Tree Depth-first Search Breadth-first Search 
#  👍 2244 👎 803

# region data
# 2021-03-24 10:47:34
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

from tree import TreeNode, stringToTreeNode


class Solution:
    # level = 0
    # res = 10 ** 5
    #
    # def minDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return self.level
    #     if not root.left and not root.right:
    #         self.res = self.level + 1 if self.level + 1 < self.res else self.res
    #
    #     if root.left:
    #         self.level += 1
    #         self.minDepth(root.left)
    #         self.level -= 1
    #     if root.right:
    #         self.level += 1
    #         self.minDepth(root.right)
    #         self.level -= 1
    #     return self.res
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = stringToTreeNode('[1,2,4,3]')
    print(Solution().minDepth(n))
