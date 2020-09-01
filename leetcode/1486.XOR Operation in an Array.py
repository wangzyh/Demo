# Given an integer n and an integer start. 
# 
#  Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.le
# ngth. 
# 
#  Return the bitwise XOR of all elements of nums. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) 
# = 8.
# Where "^" corresponds to bitwise XOR operator.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8. 
# 
#  Example 3: 
# 
#  
# Input: n = 1, start = 7
# Output: 7
#  
# 
#  Example 4: 
# 
#  
# Input: n = 10, start = 5
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1000 
#  0 <= start <= 1000 
#  n == nums.length 
#  Related Topics Array Bit Manipulation 
#  👍 206 👎 105

# region time
# 2020-09-01 19:56:17
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for x in range(n):
            res ^= (start + 2 * x)
        return res

        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 1
    start = 7
    print(Solution().xorOperation(n, start))
