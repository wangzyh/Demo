# There is an integer array nums sorted in non-decreasing order (not necessarily
#  with distinct values). 
# 
#  Before being passed to your function, nums is rotated at an unknown pivot ind
# ex k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1]
# , ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0
# ,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,
# 2,4,4]. 
# 
#  Given the array nums after the rotation and an integer target, return true if
#  target is in nums, or false if it is not in nums. 
# 
#  
#  Example 1: 
#  Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#  Example 2: 
#  Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5000 
#  -104 <= nums[i] <= 104 
#  nums is guaranteed to be rotated at some pivot. 
#  -104 <= target <= 104 
#  
# 
#  
# Follow up: This problem is the same as Search in Rotated Sorted Array, where n
# ums may contain duplicates. Would this affect the runtime complexity? How and wh
# y? Related Topics Array Binary Search 
#  👍 2045 👎 576

# region data
# 2021-04-08 15:14:11
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            if nums[0] == target:
                return True
            return False

        n = 0
        while nums[0] >= nums[-1]:
            nums.insert(0, nums.pop(-1))
            n += 1
            if n >= len(nums):
                break
        begin, last = 0, len(nums) - 1
        while begin < last:
            mid = (begin + last) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                last = mid
            else:
                begin = mid + 1
        return nums[-1] == target


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1, 1]
    m = 3
    print(Solution().search(n, m))
