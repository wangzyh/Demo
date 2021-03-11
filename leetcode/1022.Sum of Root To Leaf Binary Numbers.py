# You are given the root of a binary tree where each node has a value 0 or 1. Ea
# ch root-to-leaf path represents a binary number starting with the most significa
# nt bit. For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could repre
# sent 01101 in binary, which is 13. 
# 
#  For all leaves in the tree, consider the numbers represented by the path from
#  the root to that leaf. 
# 
#  Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits
#  integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
#  
# 
#  Example 2: 
# 
#  
# Input: root = [0]
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: 1
#  
# 
#  Example 4: 
# 
#  
# Input: root = [1,1]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 1000]. 
#  Node.val is 0 or 1. 
#  
#  Related Topics Tree 
#  👍 1082 👎 87

# region time
# 2021-03-11 22:22:30
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree import TreeNode, stringToTreeNode


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # def paths(root: TreeNode, res):
        #     if root is None:
        #         return []
        #     elif not root.left and not root.right:
        #         return [str(root.val)]
        #     else:
        #         lres = paths(root.left, res)
        #         rres = paths(root.right, res)
        #         return [str(root.val) + i for i in lres + rres]
        #
        # return sum([int(i, 2) for i in paths(root, [])])
        def paths(root, val):
            val += str(root.val)
            if root.left:
                paths(root.left, val)
            if root.right:
                paths(root.right, val)
            if not root.left and (not root.right):
                res.append(int(val, 2))

        res = []
        paths(root, '')
        return sum(res)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = '[1,0,1,0,1,0,1]'
    print(Solution().sumRootToLeaf(stringToTreeNode(n)))
