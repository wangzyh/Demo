# In a given integer array nums, there is always exactly one largest element. 
# 
#  Find whether the largest element in the array is at least twice as much as ev
# ery other number in the array. 
# 
#  If it is, return the index of the largest element, otherwise return -1. 
# 
#  Example 1: 
# 
#  
# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the array
#  x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  nums will have a length in the range [1, 50]. 
#  Every nums[i] will be an integer in the range [0, 99]. 
#  
# 
#  
#  Related Topics Array 
#  👍 387 👎 631

# region data
# 2021-01-06 11:07:08
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dominantIndex(self, nums) -> int:
        # return nums.index(max(nums)) if max(nums) / 2 in nums else -1
        maxn = max(nums)
        res = nums.index(maxn)
        nums.pop(res)
        if not nums:
            return 0
        return res if max(nums) * 2 <= maxn else -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = [3, 6, 1, 0]
    n = [3, 0, 0, 2]
    # n = [0, 0, 0, 1]
    print(Solution().dominantIndex(n))
