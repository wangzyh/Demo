# Given an array where elements are sorted in ascending order, convert it to a h
# eight balanced BST. 
# 
#  For this problem, a height-balanced binary tree is defined as a binary tree i
# n which the depth of the two subtrees of every node never differ by more than 1.
#  
# 
#  Example: 
# 
#  
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following he
# ight balanced BST:
# 
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#  
#  Related Topics Tree Depth-first Search 
#  👍 3363 👎 253

# region time
# 2021-01-28 00:02:26
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
    def sortedArrayToBST(self, nums):
        one = nums[len(nums) // 2]
        print(one)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [-10, -3, 0, 5, 9]
    print(Solution().sortedArrayToBST(n))
