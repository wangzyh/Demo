# Given the head of a linked list, remove the nth node from the end of the list 
# and return its head. 
# 
#  Follow up: Could you do this in one pass? 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1], n = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2], n = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is sz. 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
#  Related Topics Linked List Two Pointers 
#  👍 4412 👎 269

# region time
# 2020-12-29 23:01:47
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import deepcopy

from linked_list import linked_list, ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        h = head
        while head:
            if count == n:
                head.next == head.next.next
                break
            count += 1
        return h

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    head = linked_list([1, 2, 3, 4, 5])
    n = 2
    print(Solution().removeNthFromEnd(head, n))
