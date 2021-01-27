# Given n and m which are the dimensions of a matrix initialized by zeros and gi
# ven an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you 
# have to increment all cells in row ri and column ci by 1. 
# 
#  Return the number of cells with odd values in the matrix after applying the i
# ncrement to all indices. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2, m = 2, indices = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final
#  matrix.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 50 
#  1 <= m <= 50 
#  1 <= indices.length <= 100 
#  0 <= indices[i][0] < n 
#  0 <= indices[i][1] < m 
#  
#  Related Topics Array 
#  👍 403 👎 668

# region data
# 2021-01-27 12:29:08
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        # res = [[0 for j in range(m)] for i in range(n)]
        # for indice in indices:
        #     for i in range(n):
        #         res[i][indice[1]] += 1
        #     res[indice[0]] = [i + 1 for i in res[indice[0]]]
        # return [True if j % 2 != 0 else False for i in res for j in i].count(True)
        

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 13
    m = 50
    indices = [[12, 34], [10, 23], [0, 30], [12, 30], [11, 33], [8, 23], [9, 49]]
    print(Solution().oddCells(n, m, indices))
