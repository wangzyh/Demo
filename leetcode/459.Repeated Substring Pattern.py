# Given a string s, check if it can be constructed by taking a substring of it a
# nd appending multiple copies of the substring together. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aba"
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" tw
# ice.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 104 
#  s consists of lowercase English letters. 
#  
#  Related Topics String 
#  👍 2295 👎 236

# region data
# 2021-03-11 11:19:59
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # q = ''
        # for i in s:
        #     if not q or (i != q[0]):
        #         q += i
        #     else:
        #         if len(s) % len(q) == 0 and q * (len(s) // len(q)) == s:
        #             return True
        #         if len(q) * 2 > len(s):
        #             return False
        #         q += i
        # return False
        return s in (2 * s)[1:-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "abaababaab"
    print(Solution().repeatedSubstringPattern(n))
