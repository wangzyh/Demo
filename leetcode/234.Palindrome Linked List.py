# Given a singly linked list, determine if it is a palindrome. 
# 
#  Example 1: 
# 
#  
# Input: 1->2
# Output: false 
# 
#  Example 2: 
# 
#  
# Input: 1->2->2->1
# Output: true 
# 
#  Follow up: 
# Could you do it in O(n) time and O(1) space? 
#  Related Topics Linked List Two Pointers 
#  👍 4266 👎 404

# region time
# 2020-12-26 08:16:38
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = ''
    print(Solution().)
