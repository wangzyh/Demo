# Given two non-negative integers low and high. Return the count of odd numbers 
# between low and high (inclusive). 
# 
#  
#  Example 1: 
# 
#  
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7]. 
# 
#  Example 2: 
# 
#  
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9]. 
# 
#  
#  Constraints: 
# 
#  
#  0 <= low <= high <= 10^9 
#  Related Topics Math 
#  👍 63 👎 3

# region data
# 2020-07-30 15:29:05
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + (high&1) - low + (low&1)) // 2


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    low = 1
    high = 2
    print(Solution().countOdds(low, high))
