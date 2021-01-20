# Given an array of integers arr, a lucky integer is an integer which has a freq
# uency in the array equal to its value. 
# 
#  Return a lucky integer in the array. If there are multiple lucky integers ret
# urn the largest of them. If there is no lucky integer return -1. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2
# .
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.
#  
# 
#  Example 4: 
# 
#  
# Input: arr = [5]
# Output: -1
#  
# 
#  Example 5: 
# 
#  
# Input: arr = [7,7,7,7,7,7,7]
# Output: 7
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 500 
#  1 <= arr[i] <= 500 
#  Related Topics Array 
#  👍 322 👎 9

# region data
# 2021-01-20 14:38:02
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLucky(self, arr) -> int:
        from collections import Counter
        return max([key if key == value else -1 for key, value in dict(Counter(arr)).items()])


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [3]
    print(Solution().findLucky(n))
