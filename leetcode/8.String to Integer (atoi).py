# Implement atoi which converts a string to an integer. 
# 
#  The function first discards as many whitespace characters as necessary until 
# the first non-whitespace character is found. Then, starting from this character,
#  takes an optional initial plus or minus sign followed by as many numerical digi
# ts as possible, and interprets them as a numerical value. 
# 
#  The string can contain additional characters after those that form the integr
# al number, which are ignored and have no effect on the behavior of this function
# . 
# 
#  If the first sequence of non-whitespace characters in str is not a valid inte
# gral number, or if no such sequence exists because either str is empty or it con
# tains only whitespace characters, no conversion is performed. 
# 
#  If no valid conversion could be performed, a zero value is returned. 
# 
#  Note: 
# 
#  
#  Only the space character ' ' is considered as whitespace character. 
#  Assume we are dealing with an environment which could only store integers wit
# hin the 32-bit signed integer range: [−231, 231 − 1]. If the numerical value is 
# out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is
#  returned. 
#  
# 
#  Example 1: 
# 
#  
# Input: "42"
# Output: 42
#  
# 
#  Example 2: 
# 
#  
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sig
# n.
#              Then take as many numerical digits as possible, which gets 42.
#  
# 
#  Example 3: 
# 
#  
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a nume
# rical digit.
#  
# 
#  Example 4: 
# 
#  
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numeric
# al 
#              digit or a +/- sign. Therefore no valid conversion could be perfo
# rmed. 
# 
#  Example 5: 
# 
#  
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed 
# integer.
#              Thefore INT_MIN (−231) is returned. 
#  Related Topics Math String 
#  👍 1579 👎 9247


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        minus = '-'
        add = '+'
        if not str or \
                ((not str[0].isdigit() and (str[0] != add)) and (not str[0].isdigit() and (str[0] != minus))) or \
                ((str[0] == minus and len(set(str)) == 1) or (str[0] == add and len(set(str)) == 1)):
            return 0
        m = 0
        b = 0
        res = ''
        for i in str:
            if res and (not i.isdigit()):
                break
            if i == minus:
                m = 1
                b +=1
                continue
            elif i == add:
                b +=1
                continue
            elif i.isdigit():
                res += i
            elif not i.isdigit():
                break
        if b > 1:
            return 0
        if not res:
            return 0
        res = int(res) if m == 0 else int(minus + res)
        if res > 2 ** 31-1:
            res = 2 ** 31-1
        elif res < -2 ** 31:
            res = -2 ** 31
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    n = "2147483648"
    print(Solution().myAtoi(n))
