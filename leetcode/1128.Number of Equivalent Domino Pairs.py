# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = 
# [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one 
# domino can be rotated to be equal to another domino. 
# 
#  Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and
#  dominoes[i] is equivalent to dominoes[j]. 
# 
#  
#  Example 1: 
#  Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
#  
#  
#  Constraints: 
# 
#  
#  1 <= dominoes.length <= 40000 
#  1 <= dominoes[i][j] <= 9 
#  Related Topics Array 
#  👍 293 👎 147

# region data
# 2021-02-20 16:18:20
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        dominoes = list(map(sorted, dominoes))
        d = list(set(list(map(str, dominoes))))
        for i in d:
            i = [int(i[1]), int(i[-2])]
            c = dominoes.count(i)
            res += (c * c - c) // 2
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [[1, 2], [2, 1], [3, 4], [5, 6], [2, 1], [3, 4], [5, 6], [9, 2]]
    print(Solution().numEquivDominoPairs(n))
