# Given a m * n matrix of distinct numbers, return all lucky numbers in the matr
# ix in any order. 
# 
#  A lucky number is an element of the matrix such that it is the minimum elemen
# t in its row and maximum in its column. 
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row an
# d the maximum in its column
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row an
# d the maximum in its column.
#  
# 
#  Example 3: 
# 
#  
# Input: matrix = [[7,8],[1,2]]
# Output: [7]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= n, m <= 50 
#  1 <= matrix[i][j] <= 10^5. 
#  All elements in the matrix are distinct. 
#  
#  Related Topics Array 
#  👍 401 👎 39

# region data
# 2021-01-08 11:04:53
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def luckyNumbers(self, matrix):
        # res = []
        # for i in matrix:
        #     min_i = min(i)
        #     if min_i == max([j[i.index(min_i)] for j in matrix]):
        #         res.append(min_i)
        # return res
        min_m = [min(i) for i in matrix]
        max_m = [max([l[i] for l in matrix]) for i in range(len(matrix[0]))]
        return list(set(min_m) & set(max_m))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    # n = [[36376, 85652, 21002, 4510],
    #      [68246, 64237, 42962, 9974],
    #      [32768, 97721, 47338, 5841],
    #      [55103, 18179, 79062, 46542]]
    print(Solution().luckyNumbers(n))
