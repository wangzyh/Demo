# Every non-negative integer N has a binary representation. For example, 5 can b
# e represented as "101" in binary, 11 as "1011" in binary, and so on. Note that e
# xcept for N = 0, there are no leading zeroes in any binary representation. 
# 
#  The complement of a binary representation is the number in binary you get whe
# n changing every 1 to a 0 and 0 to a 1. For example, the complement of "101" in 
# binary is "010" in binary. 
# 
#  For a given number N in base-10, return the complement of it's binary represe
# ntation as a base-10 integer. 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2
#  in base-10.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: 7
# Output: 0
# Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0
#  in base-10.
#  
# 
#  
#  Example 3: 
# 
#  
# Input: 10
# Output: 5
# Explanation: 10 is "1010" in binary, with complement "0101" in binary, which i
# s 5 in base-10.
#  
# 
#  
# 
#  Note: 
# 
#  
#  0 <= N < 10^9 
#  This question is the same as 476: https://leetcode.com/problems/number-comple
# ment/ 
#  
#  
#  
#  
#  Related Topics Math 
#  👍 410 👎 43

# region data
# 2021-01-18 11:34:33
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        n = bin(N)[2:]
        return N ^ int('1' * len(n), 2)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 10
    print(Solution().bitwiseComplement(n))
