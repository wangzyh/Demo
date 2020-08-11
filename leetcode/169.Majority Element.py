# Given an array of size n, find the majority element. The majority element is t
# he element that appears more than ⌊ n/2 ⌋ times. 
# 
#  You may assume that the array is non-empty and the majority element always ex
# ist in the array. 
# 
#  Example 1: 
# 
#  
# Input: [3,2,3]
# Output: 3 
# 
#  Example 2: 
# 
#  
# Input: [2,2,1,1,1,2,2]
# Output: 2
#  
#  Related Topics Array Divide and Conquer Bit Manipulation 
#  👍 3371 👎 225

# region time
# 2020-08-09 00:03:36
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums) -> int:
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [2,2,1,1,1,2,2]
    print(Solution().majorityElement(n))
