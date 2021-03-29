# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can yo
# u climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
#  Related Topics Dynamic Programming 
#  👍 6189 👎 195

# region data
# 2021-03-26 11:32:16
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        # # 动态规划
        # if n == 1:
        #     return 1
        # dp = [0 for _ in range(n + 1)]
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 10
    print(Solution().climbStairs(n))
