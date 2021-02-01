# Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[
# i] interpreted as a binary number (from most-significant-bit to least-significan
# t-bit.) 
# 
#  Return a list of booleans answer, where answer[i] is true if and only if N_i 
# is divisible by 5. 
# 
#  Example 1: 
# 
#  
# Input: [0,1,1]
# Output: [true,false,false]
# Explanation: 
# The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10. 
#  Only the first number is divisible by 5, so answer[0] is true.
#  
# 
#  Example 2: 
# 
#  
# Input: [1,1,1]
# Output: [false,false,false]
#  
# 
#  Example 3: 
# 
#  
# Input: [0,1,1,1,1,1]
# Output: [true,false,false,false,true,false]
#  
# 
#  Example 4: 
# 
#  
# Input: [1,1,1,0,1]
# Output: [false,false,false,false,false]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 30000 
#  A[i] is 0 or 1 
#  
#  Related Topics Array 
#  👍 327 👎 102

# region data
# 2021-01-21 14:27:22
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def prefixesDivBy5(self, A):
        # A = list(map(str, A))
        # return [int(''.join(A[:i + 1]), 2) % 5 == 0 for i in range(len(A))]
        from itertools import accumulate
        return [res % 5 == 0 for res in accumulate(A, lambda base, digit: (base * 2 + digit) % 5)]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [0, 1, 1, 1, 1, 1]
    print(Solution().prefixesDivBy5(n))
