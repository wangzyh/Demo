# Given a non-empty array of integers, return the third maximum number in this a
# rray. If it does not exist, return the maximum number. The time complexity must 
# be in O(n). 
# 
#  Example 1: 
#  
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
#  
#  
# 
#  Example 2: 
#  
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned 
# instead.
#  
#  
# 
#  Example 3: 
#  
# Input: [2, 2, 3, 1]
# 
# Output: 1
# 
# Explanation: Note that the third maximum here means the third maximum distinct
#  number.
# Both numbers with value 2 are both considered as second maximum.
#  
#  Related Topics Array 
#  👍 836 👎 1515

# region time
# 2020-12-30 23:36:42
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def thirdMax(self, nums) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        nums.sort(reverse=True)
        return nums[2]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = [3, 2, 1]
    # n = [2, 2, 3, 1]
    n = [1, 1, 2]
    print(Solution().thirdMax(n))
