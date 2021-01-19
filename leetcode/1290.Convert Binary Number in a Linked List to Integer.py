# Given head which is a reference node to a singly-linked list. The value of eac
# h node in the linked list is either 0 or 1. The linked list holds the binary rep
# resentation of a number. 
# 
#  Return the decimal value of the number in the linked list. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
#  
# 
#  Example 2: 
# 
#  
# Input: head = [0]
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1]
# Output: 1
#  
# 
#  Example 4: 
# 
#  
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880
#  
# 
#  Example 5: 
# 
#  
# Input: head = [0,0]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  The Linked List is not empty. 
#  Number of nodes will not exceed 30. 
#  Each node's value is either 0 or 1. 
#  Related Topics Linked List Bit Manipulation 
#  👍 975 👎 58

# region data
# 2021-01-19 15:06:23
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from Debug.node import stringToListNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ''
        while head:
            res += f'{head.val}'
            head = head.next
        return int(res, 2)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = '[1,0,1]'
    print(Solution().getDecimalValue(stringToListNode(n)))
