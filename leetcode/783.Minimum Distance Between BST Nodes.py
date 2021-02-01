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
#  👍 909 👎 241

# region data
# 2021-01-28 17:12:45
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
    def minDiffInBST(self, root: TreeNode) -> int:
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
