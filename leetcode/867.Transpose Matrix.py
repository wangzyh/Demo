# Given a matrix A, return the transpose of A. 
# 
#  The transpose of a matrix is the matrix flipped over it's main diagonal, swit
# ching the row and column indices of the matrix. 
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
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 1000 
#  1 <= A[0].length <= 1000 
#  
#  
#  Related Topics Array 
#  👍 564 👎 324

# region data
# 2021-01-20 15:24:37
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def transpose(self, A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # n = [[1, 2, 3], [4, 5, 6]]
    print(Solution().transpose(n))
