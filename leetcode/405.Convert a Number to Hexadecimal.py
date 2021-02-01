# 
# Given an integer, write an algorithm to convert it to hexadecimal. For negativ
# e integer, two’s complement method is used.
#  
# 
#  Note:
#  
#  All letters in hexadecimal (a-f) must be in lowercase. 
#  The hexadecimal string must not contain extra leading 0s. If the number is ze
# ro, it is represented by a single zero character '0'; otherwise, the first chara
# cter in the hexadecimal string will not be the zero character. 
#  The given number is guaranteed to fit within the range of a 32-bit signed int
# eger. 
#  You must not use any method provided by the library which converts/formats th
# e number to hex directly. 
#  
#  
# 
#  Example 1:
#  
# Input:
# 26
# 
# Output:
# "1a"
#  
#  
# 
#  Example 2:
#  
# Input:
# -1
# 
# Output:
# "ffffffff"
#  
#  Related Topics Bit Manipulation 
#  👍 545 👎 126

# region data
# 2021-01-19 13:14:34
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def toHex(self, num: int) -> str:
        res = ''
        if num == 0: return '0'
        if num < 0:
            d = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                 '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
            n = bin(num & 0xffffffff)[2:]
            for i in range(0, len(n), 4):
                res += d.get(n[i:i + 4])
            return res
        d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        while num:
            if num >= 16:
                quotient = num % 16
                res += f'{quotient if quotient not in d else d.get(quotient)}'
                num //= 16
            else:
                res += f'{num if num not in d else d.get(num)}'
                break
        return res[::-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 26
    print(Solution().toHex(n))
