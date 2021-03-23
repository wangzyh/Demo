# Given the root node of a binary search tree, return the sum of values of all n
# odes with a value in the range [low, high]. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
#  
# 
#  Example 2: 
# 
#  
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 2 * 104]. 
#  1 <= Node.val <= 105 
#  1 <= low <= high <= 105 
#  All Node.val are unique. 
#  Related Topics Tree Depth-first Search Recursion 
#  👍 2165 👎 286

# region data
# 2021-03-23 16:15:23
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
    res = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        self.res += root.val if low <= root.val <= high else 0
        if root.left:
            self.rangeSumBST(root.left, low, high)
        if root.right:
            self.rangeSumBST(root.right, low, high)
        return self.res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = stringToTreeNode('[10,5,15,3,7,null,18]')
    low = 7
    high = 15
    print(Solution().rangeSumBST(n, low, high))
