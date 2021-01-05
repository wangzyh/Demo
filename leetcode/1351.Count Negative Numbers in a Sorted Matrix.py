# Given a m * n matrix grid which is sorted in non-increasing order both row-wis
# e and column-wise. 
# 
#  Return the number of negative numbers in grid. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[3,2],[1,0]]
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
#  
# 
#  Example 4: 
# 
#  
# Input: grid = [[-1]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 100 
#  -100 <= grid[i][j] <= 100 
#  Related Topics Array Binary Search 
#  👍 709 👎 43

# region data
# 2021-01-05 15:32:38
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countNegatives(self, grid) -> int:
        res, node = 0, [0, len(grid[0]) - 1]
        row = len(grid[0])
        if grid[-1][-1] >= 0:
            return res

        for i in range(len(grid)):
            node[0] = i
            if grid[i][-1] > 0:
                continue
            else:
                if grid[i][0] < 0:
                    res += row
                    continue
                if grid[i][-1] >= 0:
                    continue
                for j in range(len(grid[i]) - 1, -1, -1):
                    if grid[i][j] < 0:
                        node[1] = j
                        continue
                    res += row - node[1]
                    break
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    # grid = [[1, -1], [-1, -1], [-2, -3]]
    grid = [[5, 1, 0], [-5, -5, -5]]
    print(Solution().countNegatives(grid))
