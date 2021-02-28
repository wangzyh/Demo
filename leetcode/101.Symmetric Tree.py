# Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
#  symmetric around its center). 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 1000]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Could you solve it both recursively and iteratively? Related Topics
#  Tree Depth-first Search Breadth-first Search 
#  👍 5672 👎 153

# region time
# 2021-02-25 23:21:01
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
    def isSymmetric(self, root: TreeNode) -> bool:



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = '[1,2,2,null,3,null,3]'
    print(Solution().isSymmetric(stringToTreeNode(n)))
