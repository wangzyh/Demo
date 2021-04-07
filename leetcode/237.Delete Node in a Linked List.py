# Write a function to delete a node in a singly-linked list. You will not be giv
# en access to the head of the list, instead you will be given access to the node 
# to be deleted directly. 
# 
#  It is guaranteed that the node to be deleted is not a tail node in the list. 
# 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list shoul
# d become 4 -> 1 -> 9 after calling your function.
#  
# 
#  Example 2: 
# 
#  
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should
#  become 4 -> 5 -> 9 after calling your function.
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2,3,4], node = 3
# Output: [1,2,4]
#  
# 
#  Example 4: 
# 
#  
# Input: head = [0,1], node = 0
# Output: [1]
#  
# 
#  Example 5: 
# 
#  
# Input: head = [-3,5,-99], node = -3
# Output: [5,-99]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the given list is in the range [2, 1000]. 
#  -1000 <= Node.val <= 1000 
#  The value of each node in the list is unique. 
#  The node to be deleted is in the list and is not a tail node 
#  
#  Related Topics Linked List 
#  👍 2407 👎 8718

# region data
# 2021-03-11 13:55:20
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = ''
    print(Solution().)