# Given a string S that only contains "I" (increase) or "D" (decrease), let N = 
# S.length. 
# 
#  Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#  
# 
#  
#  If S[i] == "I", then A[i] < A[i+1] 
#  If S[i] == "D", then A[i] > A[i+1] 
#  
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "IDID"
# Output: [0,4,1,3,2]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: "III"
# Output: [0,1,2,3]
#  
# 
#  
#  Example 3: 
# 
#  
# Input: "DDI"
# Output: [3,2,0,1] 
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= S.length <= 10000 
#  S only contains characters "I" or "D". 
#  Related Topics Math 
#  👍 1072 👎 409

# region data
# 2021-02-20 09:59:48
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = [i for i in range(len(S) + 1)]
        res = []
        for i in S:
            if i == 'I':
                res.append(n[0])
                n.pop(0)
            else:
                res.append(n[-1])
                n.pop(-1)
        res.append(n[0])
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "IDID"
    print(Solution().diStringMatch(n))
