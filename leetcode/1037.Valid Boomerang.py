# A boomerang is a set of 3 points that are all distinct and not in a straight l
# ine. 
# 
#  Given a list of three points in the plane, return whether these points are a 
# boomerang. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [[1,1],[2,3],[3,2]]
# Output: true
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [[1,1],[2,2],[3,3]]
# Output: false 
#  
# 
#  
# 
#  Note: 
# 
#  
#  points.length == 3 
#  points[i].length == 2 
#  0 <= points[i][j] <= 100 
#  
# 
#  
#  
#  
#  Related Topics Math 
#  👍 145 👎 274

# region data
# 2021-02-20 10:40:18
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[1][0] - points[0][0], points[1][1] - points[0][1]
        x2, y2 = points[2][0] - points[1][0], points[2][1] - points[1][1]
        return y2 * x1 != x2 * y1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [[5, 3], [6, 3], [9, 3]]
    print(Solution().isBoomerang(n))
