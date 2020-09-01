# Given a binary tree, find its maximum depth. 
# 
#  The maximum depth is the number of nodes along the longest path from the root
#  node down to the farthest leaf node. 
# 
#  Note: A leaf is a node with no children. 
# 
#  Example: 
# 
#  Given binary tree [3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  return its depth = 3. 
#  Related Topics Tree Depth-first Search 
#  👍 2695 👎 78

# region time
# 2020-08-15 00:06:06
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            hl = self.maxDepth(root.left)
            hr = self.maxDepth(root.right)
            maxh = max(hl, hr)
            return maxh + 1
        else:
            return 0
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [3,9,20,null,null,15,7]
    print(Solution().maxDepth(n))
