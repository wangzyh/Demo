# 
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 i
# ndexed).
#  
# Once you pay the cost, you can either climb one or two steps. You need to find
#  minimum cost to reach the top of the floor, and you can either start from the s
# tep with index 0, or the step with index 1.
#  
# 
#  Example 1: 
#  
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
#  
#  
# 
#  Example 2: 
#  
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[
# 3].
#  
#  
# 
#  Note: 
#  
#  cost will have a length in the range [2, 1000]. 
#  Every cost[i] will be an integer in the range [0, 999]. 
#  
#  Related Topics Array Dynamic Programming 
#  👍 2975 👎 642

# region data
# 2021-03-26 14:21:30
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [0 for _ in range(len(cost) + 1)]
        # n = len(cost)
        # for i in range(2, n + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        # print(dp)
        # return dp[-1]
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = [1, 2, 3, 4, 5, 6]
    n = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # n = [10, 15, 20]
    print(Solution().minCostClimbingStairs(n))
