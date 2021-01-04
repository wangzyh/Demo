# Given a non-negative integer numRows, generate the first numRows of Pascal's t
# riangle. 
# 
#  
# In Pascal's triangle, each number is the sum of the two numbers directly above
#  it. 
# 
#  Example: 
# 
#  
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#  
#  Related Topics Array 
#  👍 2073 👎 123

# region data
# 2021-01-04 10:07:27
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int):
        if not numRows:
            return []
        res = [[1]]
        for i in range(numRows-1):
            res.append([sum(j) for j in zip([0] + res[i], res[i] + [0])])
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 10
    print(Solution().generate(n))
