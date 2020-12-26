# Given a Binary Search Tree (BST) with the root node root, return the minimum d
# ifference between the values of any two different nodes in the tree. 
# 
#  Example : 
# 
#  
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
# 
# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
# 
#           4
#         /   \
#       2      6
#      / \    
#     1   3  
# 
# while the minimum difference in this tree is 1, it occurs between node 1 and n
# ode 2, also between node 3 and node 2.
#  
# 
#  Note: 
# 
#  
#  The size of the BST will be between 2 and 100. 
#  The BST is always valid, each node's value is an integer, and each node's val
# ue is different. 
#  This question is the same as 530: https://leetcode.com/problems/minimum-absol
# ute-difference-in-bst/ 
#  
#  Related Topics Tree Recursion 
#  👍 847 👎 230

# region time
# 2020-12-03 23:51:39
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.Debug.tree import stringToTreeNode


class Solution:
    def minDiffInBST(self, root) -> int:
        res = 10 ** 10
        if not root:
            return res
        top = root.val
        if root.left:
            res = min(top - root.val, res)
            self.minDiffInBST(root.left)
        if root.right:
            res = min(root.val - top, res)
            self.minDiffInBST(root.right)

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    tree = '[4,2,6,1,3,5,null]'
    root = stringToTreeNode(tree)
    print(Solution().minDiffInBST(root))
