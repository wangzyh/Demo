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
#  👍 5807 👎 155

# region data
# 2021-03-24 16:23:43
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
        queue = [root]
        while queue:
            r = []
            n_q = []
            for node in queue:
                if not node:
                    r.append(None)
                else:
                    r.append(node.val)
                if hasattr(node, 'left'):
                    n_q.append(node.left)
                if hasattr(node, 'right'):
                    n_q.append(node.right)
            queue = n_q
            if r != r[::-1]:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = stringToTreeNode('[1,2,2,null,3,null,3]')
    print(Solution().isSymmetric(n))
