# The Tribonacci sequence Tn is defined as follows: 
# 
#  T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0. 
# 
#  Given n, return the value of Tn. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#  
# 
#  Example 2: 
# 
#  
# Input: n = 25
# Output: 1389537
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 37 
#  The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 -
#  1. 
#  Related Topics Recursion 
#  👍 456 👎 51

# region time
# 2021-02-07 20:33:56
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            res = [0, 1, 1]
            for i in range(3, n + 1):
                res.append(res[-1] + res[-2] + res[-3])
        return sum(res[-4:-1])

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 25
    print(Solution().tribonacci(n))
