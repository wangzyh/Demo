# Given a string s of zeros and ones, return the maximum score after splitting t
# he string into two non-empty substrings (i.e. left substring and right substring
# ). 
# 
#  The score after splitting a string is the number of zeros in the left substri
# ng plus the number of ones in the right substring. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3
#  
# 
#  Example 2: 
# 
#  
# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 
# + 3 = 5
#  
# 
#  Example 3: 
# 
#  
# Input: s = "1111"
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= s.length <= 500 
#  The string s consists of characters '0' and '1' only. 
#  
#  Related Topics String 
#  👍 280 👎 17

# region data
# 2021-01-25 15:56:01
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            if (m := s[:i].count('0') + s[i:].count('1')) > res:
                res = m
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "11"
    print(Solution().maxScore(n))
