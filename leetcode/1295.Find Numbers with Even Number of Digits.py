# Given an array nums of integers, return how many of them contain an even numbe
# r of digits.
#  
#  Example 1: 
# 
#  
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 500 
#  1 <= nums[i] <= 10^5 
#  
#  Related Topics Array 
#  👍 554 👎 70

# region data
# 2021-01-20 16:43:17
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumbers(self, nums) -> int:
        return len([i for i in nums if len(str(i)) % 2 == 0])


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [12, 345, 2, 6, 7896]
    print(Solution().findNumbers(n))
