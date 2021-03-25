# In a binary tree, the root node is at depth 0, and children of each depth k no
# de are at depth k+1. 
# 
#  Two nodes of a binary tree are cousins if they have the same depth, but have 
# different parents. 
# 
#  We are given the root of a binary tree with unique values, and the values x a
# nd y of two different nodes in the tree. 
# 
#  Return true if and only if the nodes corresponding to the values x and y are 
# cousins. 
# 
#  
# 
#  Example 1: 
#  
# 
#  
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#  
# 
#  
#  Example 2: 
#  
# 
#  
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
#  
# 
#  
#  Example 3: 
# 
#  
# 
#  
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
#  
#  
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree will be between 2 and 100. 
#  Each node has a unique integer value from 1 to 100. 
#  
#  Related Topics Tree Breadth-first Search 
#  👍 1381 👎 75

# region data
# 2021-03-24 14:15:27
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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        n = []
        queue = [[root, 0, 0], ]
        while queue:
            n_q = []
            if len(n) == 2:
                break
            for node, father, level in queue:
                if node.val == x or (node.val == y):
                    n.append([father, level])
                if node.left:
                    n_q.append([node.left, node.val, level + 1])
                if node.right:
                    n_q.append([node.right, node.val, level + 1])
            queue = n_q

        return n[0][0] != n[1][0] and (n[0][1] == n[1][1])


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = stringToTreeNode('[1,2,3,null,4,null,5]')
    print(Solution().isCousins(n, 5, 4))
