# Given two arrays of integers nums and index. Your task is to create target arr
# ay under the following rules: 
# 
#  
#  Initially target array is empty. 
#  From left to right read nums[i] and index[i], insert at index index[i] the va
# lue nums[i] in target array. 
#  Repeat the previous step until there are no elements to read in nums and inde
# x. 
#  
# 
#  Return the target array. 
# 
#  It is guaranteed that the insertion operations will be valid. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
# Output: [0,1,2,3,4]
# Explanation:
# nums       index     target
# 1            0        [1]
# 2            1        [1,2]
# 3            2        [1,2,3]
# 4            3        [1,2,3,4]
# 0            0        [0,1,2,3,4]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1], index = [0]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length, index.length <= 100 
#  nums.length == index.length 
#  0 <= nums[i] <= 100 
#  0 <= index[i] <= i 
#  
#  Related Topics Array 
#  👍 428 👎 584

# region time
# 2021-02-21 22:11:48
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res = res[:index[i]] + [nums[i]] + res[index[i]:]
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    print(Solution().createTargetArray(nums, index))
