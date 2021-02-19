# We are given two sentences A and B. (A sentence is a string of space separated
#  words. Each word consists only of lowercase letters.) 
# 
#  A word is uncommon if it appears exactly once in one of the sentences, and do
# es not appear in the other sentence. 
# 
#  Return a list of all uncommon words. 
# 
#  You may return the list in any order. 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: A = "apple apple", B = "banana"
# Output: ["banana"]
#  
# 
#  
# 
#  Note: 
# 
#  
#  0 <= A.length <= 200 
#  0 <= B.length <= 200 
#  A and B both contain only spaces and lowercase letters. 
#  
#  
#  
#  Related Topics Hash Table 
#  👍 562 👎 100

# region time
# 2021-02-19 23:58:55
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        set_A, set_B = set(A.split(' ')), set(B.split(' '))
        res = []
        for i in set_A - set_B:
            if A.split(' ').count(i) == 1:
                res.append(i)
        for i in set_B - set_A:
            if B.split(' ').count(i) == 1:
                res.append(i)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    A = "op vu kux dn jsenj hbdez hbdez nbenh z op dxmqd op"
    B = "kux wnx wnx wbi jsenj nlgfn vu f vu fvxas dn op tb"
    print(Solution().uncommonFromSentences(A, B))
