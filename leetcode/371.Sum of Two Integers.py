# Given two integers a and b, return the sum of the two integers without using t
# he operators + and -. 
# 
#  
#  Example 1: 
#  Input: a = 1, b = 2
# Output: 3
#  Example 2: 
#  Input: a = 2, b = 3
# Output: 5
#  
#  
#  Constraints: 
# 
#  
#  -1000 <= a, b <= 1000 
#  
#  Related Topics Bit Manipulation 
#  👍 1625 👎 2688

# region time
# 2021-04-07 23:57:55
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 2
    m = 3
    print(Solution().getSum(n, m))
