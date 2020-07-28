# 
# Given an unsorted array of integers, find the length of longest continuous inc
# reasing subsequence (subarray).
#  
# 
#  Example 1: 
#  
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its len
# gth is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous
#  one where 5 and 7 are separated by 4. 
#  
#  
# 
#  Example 2: 
#  
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length 
# is 1. 
#  
#  
# 
#  Note:
# Length of the array will not exceed 10,000.
#  Related Topics Array 
#  👍 806 👎 118

# region time
# 2020-07-28 23:04:36
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        res = []
        lens = 0
        for i in nums:
            if res:
                if i <= res[-1]:
                    lens = max(lens, len(res))
                    res = [i]
                    continue
            res.append(i)
        return lens
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1]
    # n = [1,3,5,4,7]
    # n = [2,2,2,2,2]
    print(Solution().findLengthOfLCIS(n))
