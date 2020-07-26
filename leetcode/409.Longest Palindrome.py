# Given a string which consists of lowercase or uppercase letters, find the leng
# th of the longest palindromes that can be built with those letters. 
# 
#  This is case sensitive, for example "Aa" is not considered a palindrome here.
#  
# 
#  Note: 
# Assume the length of given string will not exceed 1,010.
#  
# 
#  Example: 
#  
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#  
#  Related Topics Hash Table 
#  👍 961 👎 80


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = list(s)
        res = 0
        m = 0
        for i in set(s):
            if not s.count(i) % 2:
                res += s.count(i)
            if s.count(i) % 2:
                m = max(m, s.count(i))
        res += m
        return res



        
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    n = 'abccccdd'
    print(Solution().longestPalindrome(n))
