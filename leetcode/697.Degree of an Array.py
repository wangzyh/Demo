# Given a non-empty array of non-negative integers nums, the degree of this arra
# y is defined as the maximum frequency of any one of its elements. 
# 
#  Your task is to find the smallest possible length of a (contiguous) subarray 
# of nums, that has the same degree as nums. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  nums.length will be between 1 and 50,000. 
#  nums[i] will be an integer between 0 and 49,999. 
#  
#  Related Topics Array 
#  👍 1240 👎 919

# region data
# 2021-03-16 16:09:43
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        res = 50000
        d = dict(Counter(nums))
        max_v = max(d.values())
        ll = [i for i in d if d[i] == max_v]
        for i in ll:
            res = min(res, len(nums) - nums[::-1].index(i) - nums.index(i))
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1, 2]
    print(Solution().findShortestSubArray(n))
