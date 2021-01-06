# Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the n
# umber of special positions in mat. 
# 
#  A position (i,j) is called special if mat[i][j] == 1 and all other elements i
# n row i and column j are 0 (rows and columns are 0-indexed). 
# 
#  
#  Example 1: 
# 
#  
# Input: mat = [[1,0,0],
#               [0,0,1],
#               [1,0,0]]
# Output: 1
# Explanation: (1,2) is a special position because mat[1][2] == 1 and all other 
# elements in row 1 and column 2 are 0.
#  
# 
#  Example 2: 
# 
#  
# Input: mat = [[1,0,0],
#               [0,1,0],
#               [0,0,1]]
# Output: 3
# Explanation: (0,0), (1,1) and (2,2) are special positions. 
#  
# 
#  Example 3: 
# 
#  
# Input: mat = [[0,0,0,1],
#               [1,0,0,0],
#               [0,1,1,0],
#               [0,0,0,0]]
# Output: 2
#  
# 
#  Example 4: 
# 
#  
# Input: mat = [[0,0,0,0,0],
#               [1,0,0,0,0],
#               [0,1,0,0,0],
#               [0,0,1,0,0],
#               [0,0,0,1,1]]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  rows == mat.length 
#  cols == mat[i].length 
#  1 <= rows, cols <= 100 
#  mat[i][j] is 0 or 1. 
#  
#  Related Topics Array 
#  👍 178 👎 7

# region data
# 2021-01-06 14:10:28
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSpecial(self, mat) -> int:
        # res = 0
        # for i in range(len(mat)):
        #     if sum(mat[i]) != 1:
        #         continue
        #     for j in range(len(mat[i])):
        #         if mat[i][j] != 1:
        #             continue
        #         if sum([x[j] for x in mat]) != 1:
        #             continue
        #         res += 1
        #         break
        # return res
        res = 0
        for i in range(len(mat)):
            if sum(mat[i]) == 1:
                node = mat[i].index(1)
                if sum([x[node] for x in mat]) == 1:
                    res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [[1, 0, 0],
         [0, 0, 1],
         [0, 1, 0]]
    print(Solution().numSpecial(n))
