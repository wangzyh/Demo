# A binary tree is univalued if every node in the tree has the same value. 
# 
#  Return true if and only if the given tree is univalued. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [1,1,1,1,1,null,1]
# Output: true
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [2,2,2,5,2]
# Output: false
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  The number of nodes in the given tree will be in the range [1, 100]. 
#  Each node's value will be an integer in the range [0, 99]. 
#  
#  Related Topics Tree 
#  👍 749 👎 46

# region time
# 2021-02-20 20:00:17
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
    node = ''

    def isUnivalTree(self, root: TreeNode) -> bool:
        # self.node += f'{root.val} '
        # if root.left:
        #     self.isUnivalTree(root.left)
        # if root.right:
        #     self.isUnivalTree(root.right)
        # return len(set(self.node.split(' ')[:-1])) == 1
        val = root.val
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                if cur.val != val:
                    return False
                stack.append(cur.left)
                stack.append(cur.right)
        return True

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = '[58,58,58,58,null,58,58,null,null,null,58,null,null,null,58,null,58,null,58]'
    print(Solution().isUnivalTree(stringToTreeNode(n)))
