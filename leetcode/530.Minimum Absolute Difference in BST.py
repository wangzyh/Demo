# Given a binary search tree with non-negative values, find the minimum absolute
#  difference between values of any two nodes. 
# 
#  Example: 
# 
#  
# Input:
# 
#    1
#     \
#      3
#     /
#    2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 
# (or between 2 and 3).
#  
# 
#  
# 
#  Note: 
# 
#  
#  There are at least two nodes in this BST. 
#  This question is the same as 783: https://leetcode.com/problems/minimum-dista
# nce-between-bst-nodes/ 
#  
#  Related Topics Tree 
#  👍 1104 👎 85

# region data
# 2021-01-28 15:17:06
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.Debug.tree import TreeNode, stringToTreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []

        def get_all_node(root):
            res.append(root.val)
            if root.left:
                get_all_node(root.left)
            if root.right:
                get_all_node(root.right)

        get_all_node(root)
        res = sorted(res)
        return min([res[i] - res[i - 1] for i in range(len(res) - 1, 0, -1)])


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = '[4,2,6,1,3,null,null]'
    print(Solution().getMinimumDifference(stringToTreeNode(n)))
