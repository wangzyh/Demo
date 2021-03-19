# Given a string s, return the length of the longest substring between two equal
#  characters, excluding the two characters. If there is no such substring return 
# -1. 
# 
#  A substring is a contiguous sequence of characters within a string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 
# 'a's. 
# 
#  Example 2: 
# 
#  
# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
#  
# 
#  Example 3: 
# 
#  
# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
#  
# 
#  Example 4: 
# 
#  
# Input: s = "cabbac"
# Output: 4
# Explanation: The optimal substring here is "abba". Other non-optimal substring
# s include "bb" and "".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 300 
#  s contains only lowercase English letters. 
#  
#  Related Topics String 
#  👍 195 👎 12

# region data
# 2021-03-19 15:49:29
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # res = -1
        # ls = len(s)
        # for i in range(len(s)):
        #     if s.count(s[i]) >= 2:
        #         m = ls - s[::-1].index(s[i]) - s.index(s[i]) - 2
        #         res = res if res > m else m
        # return res
        return max(s.rfind(ch) - s.find(ch) - 1 for ch in set(s))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 'cababc'
    print(Solution().maxLengthBetweenEqualCharacters(n))
