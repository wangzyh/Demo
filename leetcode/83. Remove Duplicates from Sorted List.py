# 83. Remove Duplicates from Sorted List
# 2020/7/5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        if not head:
            return None
        n = p = ListNode(head.val)
        head = head.next
        while head:
            # p = p.next
            if p.val != head.val:
                p.next = ListNode(head.val)
                p = p.next
            head = head.next

        return n
        """
        if not head:
            return None

        p = head
        while p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
