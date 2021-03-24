# Given the root of a binary tree, return the level order traversal of its nodes
# ' values. (i.e., from left to right, level by level). 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: [[1]]
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 2000]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics Tree Breadth-first Search 
#  👍 4408 👎 104

# region data
# 2021-03-23 16:42:38
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from tree import TreeNode, stringToTreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            r = []
            n_q = []
            for point in queue:
                r.append(point.val)
                if point.left:
                    n_q.append(point.left)
                if point.right:
                    n_q.append(point.right)
            res.append(r)
            queue = n_q
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = stringToTreeNode('[3,9,20,null,null,15,7]')
    print(Solution().levelOrder(n))
