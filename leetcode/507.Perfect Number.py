# A perfect number is a positive integer that is equal to the sum of its positiv
# e divisors, excluding the number itself. A divisor of an integer x is an integer
#  that can divide x evenly. 
# 
#  Given an integer n, return true if n is a perfect number, otherwise return fa
# lse. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 6
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: num = 496
# Output: true
#  
# 
#  Example 4: 
# 
#  
# Input: num = 8128
# Output: true
#  
# 
#  Example 5: 
# 
#  
# Input: num = 2
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 108 
#  
#  Related Topics Math 
#  👍 355 👎 699

# region data
# 2021-02-19 16:44:48
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # if num == 1:
        #     return False
        # res = {1}
        # for i in range(2, num // 2 + 1):
        #     if num % i == 0:
        #         res.add(i)
        #         res.add(num // i)
        #
        # return sum(res) == num
        return num in [6, 28, 496, 8128, 33550336]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 99999993
    print(Solution().checkPerfectNumber(n))
