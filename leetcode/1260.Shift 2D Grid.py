# Given a 2D grid of size m x n and an integer k. You need to shift the grid k t
# imes. 
# 
#  In one shift operation: 
# 
#  
#  Element at grid[i][j] moves to grid[i][j + 1]. 
#  Element at grid[i][n - 1] moves to grid[i + 1][0]. 
#  Element at grid[m - 1][n - 1] moves to grid[0][0]. 
#  
# 
#  Return the 2D grid after applying shift operation k times. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m <= 50 
#  1 <= n <= 50 
#  -1000 <= grid[i][j] <= 1000 
#  0 <= k <= 100 
#  
#  Related Topics Array 
#  👍 292 👎 111

# region data
# 2021-01-28 13:56:12
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shiftGrid(self, grid, k: int):
        while k:
            for i in range(len(grid)):
                if i + 1 >= len(grid):
                    grid[0].insert(0, grid[i][-1])
                else:
                    grid[i + 1].insert(0, grid[i][-1])
                grid[i].pop(-1)
            k -= 1
        return grid


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 3
    print(Solution().shiftGrid(grid, k))
