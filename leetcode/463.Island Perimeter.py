# You are given row x col grid representing a map where grid[i][j] = 1 represent
# s land and grid[i][j] = 0 represents water. 
# 
#  Grid cells are connected horizontally/vertically (not diagonally). The grid i
# s completely surrounded by water, and there is exactly one island (i.e., one or 
# more connected land cells). 
# 
#  The island doesn't have "lakes", meaning the water inside isn't connected to 
# the water around the island. One cell is a square with side length 1. The grid i
# s rectangular, width and height don't exceed 100. Determine the perimeter of the
#  island. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[1]]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,0]]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  row == grid.length 
#  col == grid[i].length 
#  1 <= row, col <= 100 
#  grid[i][j] is 0 or 1. 
#  
#  Related Topics Hash Table 
#  👍 2484 👎 132

# region data
# 2021-01-12 09:57:31
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def islandPerimeter(self, grid) -> int:
        res, adj = 0, 0
        for i in range(len(grid)):
            res += grid[i].count(1)
            for j in range(len(grid[0])):
                if j + 1 < len(grid[0]) and grid[i][j] and grid[i][j + 1] == 1:
                    adj += 1
                if i + 1 < len(grid) and grid[i][j] and grid[i + 1][j] == 1:
                    adj += 1
        return res * 4 - adj * 2


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    n = [[1]]
    # n = [[1], [1]]
    print(Solution().islandPerimeter(n))
