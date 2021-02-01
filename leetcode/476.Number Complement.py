# Given a positive integer num, output its complement number. The complement str
# ategy is to flip the bits of its binary representation. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and
#  its complement is 010. So you need to output 2.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and i
# ts complement is 0. So you need to output 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  The given integer num is guaranteed to fit within the range of a 32-bit signe
# d integer. 
#  num >= 1 
#  You could assume no leading zero bit in the integer’s binary representation. 
# 
#  This question is the same as 1009: https://leetcode.com/problems/complement-o
# f-base-10-integer/ 
#  
#  Related Topics Bit Manipulation 
#  👍 1070 👎 85

# region data
# 2021-01-18 10:49:03
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findComplement(self, num: int) -> int:
        n = bin(num)[2:]
        return num ^ int('1' * len(n), 2)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 156
    print(Solution().findComplement(n))
