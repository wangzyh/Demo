# Given alphanumeric string s. (Alphanumeric string is a string consisting of lo
# wercase English letters and digits). 
# 
#  You have to find a permutation of the string where no letter is followed by a
# nother letter and no digit is followed by another digit. That is, no two adjacen
# t characters have the same type. 
# 
#  Return the reformatted string or return an empty string if it is impossible t
# o reformat the string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c
# 2", "0a1b2c", "0c2a1b" are also valid permutations.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by digi
# ts.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by charac
# ters.
#  
# 
#  Example 4: 
# 
#  
# Input: s = "covid2019"
# Output: "c2o0v1i9d"
#  
# 
#  Example 5: 
# 
#  
# Input: s = "ab123"
# Output: "1a2b3"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 500 
#  s consists of only lowercase English letters and/or digits. 
#  
#  Related Topics String 
#  👍 206 👎 50

# region data
# 2021-01-26 13:50:44
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reformat(self, s: str) -> str:
        # res = [''] * len(s)
        # num = []
        # letter = []
        # for i in s:
        #     if 97 <= ord(i) <= 122:
        #         letter.append(i)
        #     else:
        #         num.append(i)
        # if len(letter) == len(num) + 1:
        #     n = 0
        #     for i in range(0, len(s), 2):
        #         res[i] = letter[n]
        #         if n >= len(num):
        #             return ''.join(res)
        #         res[i + 1] = num[n]
        #         n += 1
        # elif len(letter) + 1 == len(num):
        #     n = 0
        #     for i in range(0, len(s), 2):
        #         res[i] = num[n]
        #         if n >= len(letter):
        #             return ''.join(res)
        #         res[i + 1] = letter[n]
        #         n += 1
        # elif len(letter) == len(num):
        #     n = 0
        #     for i in range(0, len(s), 2):
        #         res[i] = num[n]
        #         res[i + 1] = letter[n]
        #         n += 1
        #     return ''.join(res)
        # return ''
        a = list(filter(str.isalpha, s))
        b = list(filter(str.isdigit, s))
        if len(b) > len(a):
            a, b = b, a
        if len(a) - len(b) > 1:
            return ""
        ans = ""
        for i in range(len(a)):
            ans += a[i]
            if i < len(b):
                ans += b[i]
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "a0b1c2"
    print(Solution().reformat(n))
