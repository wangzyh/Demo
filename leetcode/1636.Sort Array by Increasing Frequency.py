# Given an array of integers nums, sort the array in increasing order based on t
# he frequency of the values. If multiple values have the same frequency, sort the
# m in decreasing order. 
# 
#  Return the sorted array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a
#  frequency of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in dec
# reasing order.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1] 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  -100 <= nums[i] <= 100 
#  
#  Related Topics Array Sort 
#  👍 239 👎 9

# region data
# 2021-01-22 16:43:57
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def frequencySort(self, nums):
        from collections import Counter
        d = sorted(dict(Counter(sorted(nums, reverse=True))).items(), key=lambda x: x[1])
        return [str(key[0]) for key in d for j in range(key[1])]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(Solution().frequencySort(n))
