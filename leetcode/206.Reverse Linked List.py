# Given the head of a singly linked list, reverse the list, and return the rever
# sed list. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2]
# Output: [2,1]
#  
# 
#  Example 3: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is the range [0, 5000]. 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
#  Follow up: A linked list can be reversed either iteratively or recursively. C
# ould you implement both? 
#  Related Topics Linked List 
#  👍 6513 👎 123

# region time
# 2021-03-13 00:16:32
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linked_list import ListNode, stringToListNode


class Solution:
    r = res = ListNode(0)

    def reverseList(self, head: ListNode) -> ListNode:
        if head.next:
            self.reverseList(head.next)

        self.res.next = head
        self.res = self.res.next
        return self.r.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = '123'
    print(Solution().reverseList(stringToListNode(n)))
