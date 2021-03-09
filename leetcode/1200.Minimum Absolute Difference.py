# Given an array of distinct integers arr, find all pairs of elements with the m
# inimum absolute difference of any two elements. 
# 
#  Return a list of pairs in ascending order(with respect to pairs), each pair [
# a, b] follows 
# 
#  
#  a, b are from arr 
#  a < b 
#  b - a equals to the minimum absolute difference of any two elements in arr 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with differe
# nce equal to 1 in ascending order. 
# 
#  Example 2: 
# 
#  
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= arr.length <= 10^5 
#  -10^6 <= arr[i] <= 10^6 
#  
#  Related Topics Array 
#  👍 545 👎 28

# region time
# 2021-03-08 00:55:52
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        minimum = min(diff)
        return [[arr[i], arr[i + 1]] for i in range(len(diff)) if diff[i] == minimum]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [3, 8, -10, 23, 19, -4, -14, 27]
    print(Solution().minimumAbsDifference(n))
