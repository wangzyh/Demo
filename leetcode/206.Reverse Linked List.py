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
#  👍 6584 👎 125

# region time
# 2021-03-24 18:49:09
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Debug.linked_list import ListNode, stringToListNode, prettyPrintLinkedList


class Solution:
    # r = res = ListNode(0)

    def reverseList(self, head: ListNode) -> ListNode:
        # queue = [head]
        # while queue:
        #     node = queue.pop(0)
        #     if not node:
        #         return node
        #     self.reverseList(node.next)
        #     self.res.next = ListNode(node.val)
        #     self.res = self.res.next
        # return self.r.next
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = stringToListNode('12345')
    prettyPrintLinkedList(Solution().reverseList(n))
