# Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
#  
# 
#  Notice that the row index starts from 0. 
# 
#  
# In Pascal's triangle, each number is the sum of the two numbers directly above
#  it. 
# 
#  Follow up: 
# 
#  Could you optimize your algorithm to use only O(k) extra space? 
# 
#  
#  Example 1: 
#  Input: rowIndex = 3
# Output: [1,3,3,1]
#  Example 2: 
#  Input: rowIndex = 0
# Output: [1]
#  Example 3: 
#  Input: rowIndex = 1
# Output: [1,1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= rowIndex <= 33 
#  
#  Related Topics Array 
#  👍 1193 👎 215

# region data
# 2021-01-14 09:58:06
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int):
        if not rowIndex:
            return [1]
        res = [[1]]
        for i in range(rowIndex):
            res.append([sum(j) for j in zip([0] + res[i], res[i] + [0])])
        return res[-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 3
    print(Solution().getRow(n))
