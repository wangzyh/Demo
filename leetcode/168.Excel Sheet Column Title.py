# Given a positive integer, return its corresponding column title as appear in a
# n Excel sheet. 
# 
#  For example: 
# 
#  
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
#  
# 
#  Example 1: 
# 
#  
# Input: 1
# Output: "A"
#  
# 
#  Example 2: 
# 
#  
# Input: 28
# Output: "AB"
#  
# 
#  Example 3: 
# 
#  
# Input: 701
# Output: "ZY"
#  Related Topics Math 
#  👍 1218 👎 250

# region time
# 2020-07-31 22:18:37
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToTitle(self, n: int) -> str:
        if not n:
            return ''
        d = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
             11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
             20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
        if n <= 26:
            return d[n]
        res = d[n % 26 if n % 26 > 0 else 26]
        return self.convertToTitle((n // 26) if n % 26 != 0 else (n // 26 - 1)) + res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = 52
    n = 5322
    # n = 204
    print(Solution().convertToTitle(n))
