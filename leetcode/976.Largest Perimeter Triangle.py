# Given an array A of positive lengths, return the largest perimeter of a triang
# le with non-zero area, formed from 3 of these lengths. 
# 
#  If it is impossible to form any triangle of non-zero area, return 0. 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [2,1,2]
# Output: 5
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [1,2,1]
# Output: 0
#  
# 
#  
#  Example 3: 
# 
#  
# Input: [3,2,3,4]
# Output: 10
#  
# 
#  
#  Example 4: 
# 
#  
# Input: [3,6,2,3]
# Output: 8
#  
# 
#  
# 
#  Note: 
# 
#  
#  3 <= A.length <= 10000 
#  1 <= A[i] <= 10^6 
#  
#  
#  
#  
#  Related Topics Math Sort 
#  👍 487 👎 52

# region data
# 2021-02-20 15:04:55
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2] and A[i] - A[i + 1] < A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [3, 6, 2, 3]
    print(Solution().largestPerimeter(n))
