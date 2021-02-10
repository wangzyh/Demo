# Given a string S of lowercase letters, a duplicate removal consists of choosin
# g two adjacent and equal letters, and removing them. 
# 
#  We repeatedly make duplicate removals on S until we no longer can. 
# 
#  Return the final string after all such duplicate removals have been made. It 
# is guaranteed the answer is unique. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent a
# nd equal, and this is the only possible move.  The result of this move is that t
# he string is "aaca", of which only "aa" is possible, so the final string is "ca"
# .
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= S.length <= 20000 
#  S consists only of English lowercase letters. 
#  
#  Related Topics Stack 
#  👍 1311 👎 89

# region time
# 2021-02-08 00:17:34
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, S: str) -> str:
        q = []
        for i in S:
            if q and i == q[-1]:
                while q and i == q[-1]:
                    q.pop()
            else:
                q.append(i)
        return ''.join(q)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 'abbaca'
    print(Solution().removeDuplicates(n))
