# Given the roots of two binary trees p and q, write a function to check if they
#  are the same or not. 
# 
#  Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value. 
# 
#  
#  Example 1: 
# 
#  
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: p = [1,2], q = [1,null,2]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both trees is in the range [0, 100]. 
#  -104 <= Node.val <= 104 
#  
#  Related Topics Tree Depth-first Search 
#  👍 2858 👎 77

# region time
# 2021-01-27 21:32:50
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    p = '[1,2,3]'
    q = '[1,2,3]'
    print(Solution().isSameTree(stringToTreeNode(p), stringToTreeNode(q)))
