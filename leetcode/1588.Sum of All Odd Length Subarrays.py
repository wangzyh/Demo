# Given an array of positive integers arr, calculate the sum of all possible odd
# -length subarrays. 
# 
#  A subarray is a contiguous subsequence of the array. 
# 
#  Return the sum of all odd-length subarrays of arr. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58 
# 
# 
#  Example 2: 
# 
#  
# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum 
# is 3. 
# 
#  Example 3: 
# 
#  
# Input: arr = [10,11,12]
# Output: 66
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 100 
#  1 <= arr[i] <= 1000 
#  
#  Related Topics Array 
#  👍 626 👎 75

# region data
# 2021-03-22 10:49:10
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # num = 3
        # res = sum(arr)
        # while num <= len(arr):
        #     for i in range(len(arr)):
        #         if i + num < len(arr) + 1:
        #             res += sum(arr[i:i + num])
        #     num += 2
        # return res
        res = 0

        # Size of array
        l = len(arr)

        # Traverse the given array arr[]
        for i in range(l):
            # Add to the sum for each
            # contribution of the arr[i]
            res += ((((i + 1) * (l - i) + 1) // 2) * arr[i])

        # Return the final sum
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [10, 11, 12]
    print(Solution().sumOddLengthSubarrays(n))
