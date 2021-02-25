# Given a binary tree, return all root-to-leaf paths. 
# 
#  Note: A leaf is a node with no children. 
# 
#  Example: 
# 
#  
# Input:
# 
#    1
#  /   \
# 2     3
#  \
#   5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#  Related Topics Tree Depth-first Search 
#  👍 2377 👎 125

# region time
# 2021-02-25 21:32:09
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # res = []
        #
        # def get_path(root: TreeNode, data: List):
        #     if not root:
        #         return []
        #     data.append(f'{root.val}')
        #     if root.left:
        #         tmp = data.copy()
        #         get_path(root.left, tmp)
        #     if root.right:
        #         tmp = data.copy()
        #         get_path(root.right, tmp)
        #
        #     else:
        #         if root.left is None and (root.right is None):
        #             res.append('->'.join(data))
        #
        # get_path(root, [])
        # return res
        if root is None:
            return []
        elif not root.left and not root.right:
            return [root.val]
        else:
            lstr = self.binaryTreePaths(root.left)
            rstr = self.binaryTreePaths(root.right)
            return [f'{root.val}->{i}' for i in lstr + rstr]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = '[1,2,null,3]'
    n = '[1,2,3,4,5,6,7,8]'
    print(Solution().binaryTreePaths(stringToTreeNode(n)))
