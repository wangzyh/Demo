# Given an integer n. No-Zero integer is a positive integer which doesn't contai
# n any 0 in its decimal representation. 
# 
#  Return a list of two integers [A, B] where: 
# 
#  
#  A and B are No-Zero integers. 
#  A + B = n 
#  
# 
#  It's guarateed that there is at least one valid solution. If there are many v
# alid solutions you can return any of them. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: [1,1]
# Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in t
# heir decimal representation.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 11
# Output: [2,9]
#  
# 
#  Example 3: 
# 
#  
# Input: n = 10000
# Output: [1,9999]
#  
# 
#  Example 4: 
# 
#  
# Input: n = 69
# Output: [1,68]
#  
# 
#  Example 5: 
# 
#  
# Input: n = 1010
# Output: [11,999]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= n <= 10^4 
#  Related Topics Math 
#  👍 141 👎 141

# region time
# 2021-01-17 23:00:19
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getNoZeroIntegers(self, n: int):
        for i in range(1, n // 2+1):
            if '0' not in str(i) and '0' not in str(n - i):
                return [i, n - i]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 2
    print(Solution().getNoZeroIntegers(n))
