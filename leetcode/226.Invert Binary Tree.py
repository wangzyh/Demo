# Given the root of a binary tree, invert the tree, and return its root. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,1,3]
# Output: [2,3,1]
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree 
#  👍 4917 👎 72

# region time
# 2021-03-20 19:38:09
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree import TreeNode, stringToTreeNode, prettyPrintTree


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # if root is None:
        #     return None
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # root.left, root.right = root.right, root.left
        # return root
        if root:
            node = TreeNode(root.val)
            node.left, node.right = self.invertTree(root.right), self.invertTree(root.left)
            return node
        return None


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = stringToTreeNode('[4,2,7,1,3,6,9]')
    print(prettyPrintTree(Solution().invertTree(n)))
