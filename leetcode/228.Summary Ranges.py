# You are given a sorted unique integer array nums. 
# 
#  Return the smallest sorted list of ranges that cover all the numbers in the a
# rray exactly. That is, each element of nums is covered by exactly one of the ran
# ges, and there is no integer x such that x is in one of the ranges but not in nu
# ms. 
# 
#  Each range [a,b] in the list should be output as: 
# 
#  
#  "a->b" if a != b 
#  "a" if a == b 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#  
# 
#  Example 3: 
# 
#  
# Input: nums = []
# Output: []
#  
# 
#  Example 4: 
# 
#  
# Input: nums = [-1]
# Output: ["-1"]
#  
# 
#  Example 5: 
# 
#  
# Input: nums = [0]
# Output: ["0"]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 20 
#  -231 <= nums[i] <= 231 - 1 
#  All the values of nums are unique. 
#  nums is sorted in ascending order. 
#  
#  Related Topics Array 
#  👍 932 👎 674

# region time
# 2021-02-19 20:59:46
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # if len(nums) == 0:
        #     return []
        # if len(nums) == 1:
        #     return [str(nums[0])]
        # res = []
        # diff = list(set([i for i in range(nums[0] - 1, nums[-1])]) - set(nums[:-1]))
        # diff.append(nums[-1] + 1)
        # diff.sort()
        # print(diff)
        # for i in range(len(diff) - 1):
        #     res.append([diff[i] + 1, diff[i + 1] - 1] if diff[i] + 1 != diff[i + 1] - 1 else diff[i] + 1)
        # return [f'{i[0]}->{i[1]}' if not isinstance(i, int) else f'{i}' for i in res]
        # leetcode submit region end(Prohibit modification and deletion)
        res = []
        tmp = []
        for i in range(len(nums)):
            if i + 1 == len(nums):
                if tmp:
                    tmp.append(nums[i])
                    res.append(tmp)
                    break
                res.append([nums[i]])
                break
            tmp.append(nums[i])
            if nums[i] + 1 != nums[i + 1]:
                res.append(tmp)
                tmp = []
        return [f'{i[0]}->{i[-1]}' if len(i) != 1 else f'{i[0]}' for i in res]


if __name__ == '__main__':
    n = [0, 2, 3, 4, 6, 8, 9]
    print(Solution().summaryRanges(n))
