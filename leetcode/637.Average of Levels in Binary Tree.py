# Given the root of a binary tree, return the average value of the nodes on each
#  level in the form of an array. Answers within 10-5 of the actual answer will be
#  accepted.
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, a
# nd on level 2 is 11.
# Hence return [3, 14.5, 11].
#  
# 
#  Example 2: 
# 
#  
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 104]. 
#  -231 <= Node.val <= 231 - 1 
#  
#  Related Topics Tree 
#  👍 1926 👎 201

# region data
# 2021-03-24 13:39:03
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            r = 0
            n_q = []
            for node in queue:
                r += node.val
                if node.right:
                    n_q.append(node.right)
                if node.left:
                    n_q.append(node.left)
            res.append(r / len(queue))
            queue = n_q

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = stringToTreeNode('[3,9,20,null,15,7]')
    print(Solution().averageOfLevels(n))
