# An array is monotonic if it is either monotone increasing or monotone decreasi
# ng. 
# 
#  An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A
#  is monotone decreasing if for all i <= j, A[i] >= A[j]. 
# 
#  Return true if and only if the given array A is monotonic. 
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
# Input: [1,2,2,3]
# Output: true
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [6,5,4,4]
# Output: true
#  
# 
#  
#  Example 3: 
# 
#  
# Input: [1,3,2]
# Output: false
#  
# 
#  
#  Example 4: 
# 
#  
# Input: [1,2,4,5]
# Output: true
#  
# 
#  
#  Example 5: 
# 
#  
# Input: [1,1,1]
# Output: true
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 50000 
#  -100000 <= A[i] <= 100000 
#  
#  
#  
#  
#  
#  
#  Related Topics Array 
#  👍 875 👎 40

# region time
# 2021-01-24 23:36:10
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMonotonic(self, A) -> bool:
        # return A == sorted(A) or (A == sorted(A, reverse=True))
        a = sorted(A)
        return A == a or (A == a[::-1])


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [6, 5, 4, 4]
    print(Solution().isMonotonic(n))
