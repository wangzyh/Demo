# We define a harmonious array as an array where the difference between its maxi
# mum value and its minimum value is exactly 1. 
# 
#  Given an integer array nums, return the length of its longest harmonious subs
# equence among all its possible subsequences. 
# 
#  A subsequence of array is a sequence that can be derived from the array by de
# leting some or no elements without changing the order of the remaining elements.
#  
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4]
# Output: 2
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,1,1,1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 104 
#  -109 <= nums[i] <= 109 
#  
#  Related Topics Hash Table 
#  👍 1133 👎 120

# region time
# 2021-03-07 22:03:15
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        longest = 0
        set_n = set(nums)
        for i in set_n:
            if i + 1 in set_n:
                longest = max(longest, d[i] + d[i + 1])
            if i - 1 in set_n:
                longest = max(longest, d[i] + d[i - 1])
        return longest


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1, 3, 2, 2, 5, 2, 3, 7]
    print(Solution().findLHS(n))
