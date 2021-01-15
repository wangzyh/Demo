# Given a square matrix mat, return the sum of the matrix diagonals. 
# 
#  Only include the sum of all the elements on the primary diagonal and all the 
# elements on the secondary diagonal that are not part of the primary diagonal. 
# 
#  
#  Example 1: 
# 
#  
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
#  
# 
#  Example 2: 
# 
#  
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
#  
# 
#  Example 3: 
# 
#  
# Input: mat = [[5]]
# Output: 5
#  
# 
#  
#  Constraints: 
# 
#  
#  n == mat.length == mat[i].length 
#  1 <= n <= 100 
#  1 <= mat[i][j] <= 100 
#  
#  Related Topics Array 
#  👍 311 👎 8

# region data
# 2021-01-14 16:47:22
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diagonalSum(self, mat) -> int:
        len_m = len(mat)
        node_r = [mat[i][len_m - 1 - i] for i in range(len_m) if i != len_m - 1 - i]
        node_l = [mat[i][i] for i in range(len_m)]
        return sum(node_l + node_r)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = [[1, 2, 3],
    #      [4, 5, 6],
    #      [7, 8, 9]]
    n = [[1, 32, 32, 22, 21, 12],
         [1, 32, 92, 22, 21, 12],
         [1, 32, 2, 22, 21, 12],
         [1, 32, 32, 22, 21, 12],
         [1, 32, 32, 22, 21, 12],
         [1, 32, 22, 22, 21, 12]]
    print(Solution().diagonalSum(n))
