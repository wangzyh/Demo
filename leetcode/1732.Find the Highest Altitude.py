# There is a biker going on a road trip. The road trip consists of n + 1 points 
# at different altitudes. The biker starts his trip on point 0 with altitude equal
#  0. 
# 
#  You are given an integer array gain of length n where gain[i] is the net gain
#  in altitude between points i and i + 1 for all (0 <= i < n). Return the highest
#  altitude of a point. 
# 
#  
#  Example 1: 
# 
#  
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
#  
# 
#  Example 2: 
# 
#  
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == gain.length 
#  1 <= n <= 100 
#  -100 <= gain[i] <= 100 
#  
#  Related Topics Array 
#  👍 72 👎 5

# region data
# 2021-01-27 16:24:32
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestAltitude(self, gain) -> int:
        res = [0]
        for i in gain:
            res.append(res[-1] + i)
        return max(res)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [-5, 1, 5, 0, -7]
    print(Solution().largestAltitude(n))
