# Given an array of integers nums. 
# 
#  A pair (i,j) is called good if nums[i] == nums[j] and i < j. 
# 
#  Return the number of good pairs. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,2,3]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  1 <= nums[i] <= 100 
#  Related Topics Array Hash Table Math 
#  👍 261 👎 12

# region data
# 2020-07-31 11:30:03
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIdenticalPairs(self, nums) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1, 1, 1, 1]
    print(Solution().numIdenticalPairs(n))
