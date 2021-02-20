# Given a string s, determine if it is a palindrome, considering only alphanumer
# ic characters and ignoring cases. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2 * 105 
#  s consists only of printable ASCII characters. 
#  
#  Related Topics Two Pointers String 
#  👍 1760 👎 3592

# region data
# 2021-02-20 09:28:19
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s.lower():
            if i.isalnum():
                res += i
        return res == res[::-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(n))
