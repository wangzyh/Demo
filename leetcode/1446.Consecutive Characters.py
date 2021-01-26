# Given a string s, the power of the string is the maximum length of a non-empty
#  substring that contains only one unique character. 
# 
#  Return the power of the string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
# 
#  
# 
#  Example 3: 
# 
#  
# Input: s = "triplepillooooow"
# Output: 5
#  
# 
#  Example 4: 
# 
#  
# Input: s = "hooraaaaaaaaaaay"
# Output: 11
#  
# 
#  Example 5: 
# 
#  
# Input: s = "tourist"
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 500 
#  s contains only lowercase English letters. 
#  Related Topics String 
#  👍 445 👎 12

# region data
# 2021-01-26 12:41:38
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPower(self, s: str) -> int:
        res = 0
        l = []
        for i in s:
            if not l:
                l.append(i)
                continue
            if i == l[-1]:
                l.append(i)
            else:
                res = max(res, len(l))
                l = [i]
        return max(res, len(l))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "cc"
    print(Solution().maxPower(n))
