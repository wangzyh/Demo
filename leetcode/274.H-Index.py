# Given an array of integers citations where citations[i] is the number of citat
# ions a researcher received for their ith paper, return compute the researcher's 
# h-index. 
# 
#  According to the definition of h-index on Wikipedia: A scientist has an index
#  h if h of their n papers have at least h citations each, and the other n − h pa
# pers have no more than h citations each. 
# 
#  If there are several possible values for h, the maximum one is taken as the h
# -index. 
# 
#  
#  Example 1: 
# 
#  
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each o
# f them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remai
# ning two with no more than 3 citations each, their h-index is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: citations = [1,3,1]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  n == citations.length 
#  1 <= n <= 5000 
#  0 <= citations[i] <= 1000 
#  
#  Related Topics Hash Table Sort 
#  👍 898 👎 1480

# region data
# 2021-04-20 11:19:30
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 0
        for i, v in enumerate(citations):
            if v > i:
                res += 1

        return res

        # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [3, 0, 6, 1, 5]
    print(Solution().hIndex(n))
