# Given a binary matrix A, we want to flip the image horizontally, then invert i
# t, and return the resulting image. 
# 
#  To flip an image horizontally means that each row of the image is reversed. F
# or example, flipping [1, 1, 0] horizontally results in [0, 1, 1]. 
# 
#  To invert an image means that each 0 is replaced by 1, and each 1 is replaced
#  by 0. For example, inverting [0, 1, 1] results in [1, 0, 0]. 
# 
#  Example 1: 
# 
#  
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]
# .
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#  
# 
#  Notes: 
# 
#  
#  1 <= A.length = A[0].length <= 20 
#  0 <= A[i][j] <= 1 
#  
#  Related Topics Array 
#  👍 1188 👎 171

# region time
# 2021-01-07 20:59:40
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def flipAndInvertImage(self, A):
        # return [[x ^ 1 for x in j] for i in A for j in [i[::-1]]]
        return [[i ^ 1 for i in row[::-1]] for row in A]
        # return list(map(lambda x: list(map(lambda y: 1 if y == 0 else 0, x[::-1])), A))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(Solution().flipAndInvertImage(n))
