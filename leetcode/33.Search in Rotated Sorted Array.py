# There is an integer array nums sorted in ascending order (with distinct values
# ). 
# 
#  Prior to being passed to your function, nums is rotated at an unknown pivot i
# ndex k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+
# 1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, 
# [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. 
# 
#  Given the array nums after the rotation and an integer target, return the ind
# ex of target if it is in nums, or -1 if it is not in nums. 
# 
#  
#  Example 1: 
#  Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#  Example 2: 
#  Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#  Example 3: 
#  Input: nums = [1], target = 0
# Output: -1
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5000 
#  -104 <= nums[i] <= 104 
#  All values of nums are unique. 
#  nums is guaranteed to be rotated at some pivot. 
#  -104 <= target <= 104 
#  
# 
#  
# Follow up: Can you achieve this in O(log n) time complexity? Related Topics Ar
# ray Binary Search 
#  👍 7340 👎 643

# region data
# 2021-04-06 15:54:58
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target not in nums:
        #     return -1
        # return nums.index(target)
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                for j in nums[::-1]:
                    if j == target:
                        return nums.index(j)
        return -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [4, 5, 6, 7, 0, 1, 2]
    target = 6
    print(Solution().search(n, target))
