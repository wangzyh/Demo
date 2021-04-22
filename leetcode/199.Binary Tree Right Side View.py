# Given the root of a binary tree, imagine yourself standing on the right side o
# f it, return the values of the nodes you can see ordered from top to bottom. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,null,3]
# Output: [1,3]
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
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree Depth-first Search Breadth-first Search Recursion Queue 
#  👍 3776 👎 201

# region data
# 2021-04-20 12:42:13
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            r = []
            v = []
            for q in queue:
                r.append(q.val)

                if q.left:
                    v.append(q.left)
                if q.right:
                    v.append(q.right)
            res.append(r[-1])
            queue = v
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = '[1,2,3,4]'
    print(Solution().rightSideView(stringToTreeNode(n)))
