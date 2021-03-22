# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (
# t concatenated with itself 1 or more times) 
# 
#  Given two strings str1 and str2, return the largest string x such that x divi
# des both str1 and str2. 
# 
#  
#  Example 1: 
#  Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#  Example 2: 
#  Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#  Example 3: 
#  Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#  Example 4: 
#  Input: str1 = "ABCDEF", str2 = "ABC"
# Output: ""
#  
#  
#  Constraints: 
# 
#  
#  1 <= str1.length <= 1000 
#  1 <= str2.length <= 1000 
#  str1 and str2 consist of English uppercase letters. 
#  
#  Related Topics String 
#  👍 751 👎 174

# region time
# 2021-03-21 14:05:51
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if (len(str1) // len(str2)) * str2 == str1:
        #     return str2
        #
        # s = ''
        # for i in range(len(str2)):
        #     if str2.count(str2[i]) == 1 or (len(str2) < 2 * i):
        #         s = ''
        #         break
        #     s += str2[i]
        #     if (len(str2) // len(s)) * s == str2:
        #         break
        # if s:
        #     if (len(str1) // len(s)) * s == str1:
        #         return s * (math.gcd(len(str1) // len(s), len(str2) // len(s)))
        # return ''
        if str2 + str1 == str1 + str2:
            return str1[:math.gcd(len(str1), len(str2))]
        else:
            return ''


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 'ABCABCABCABCABCABC'
    m = 'ABCABCABCABC'
    print(Solution().gcdOfStrings(n, m))
